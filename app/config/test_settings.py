"""Settings contract tests; no Django setup, driver or database is required."""

import os
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch

from django.core.exceptions import DisallowedHost, ImproperlyConfigured
from django.http import HttpRequest
from django.test import override_settings


SETTINGS = Path(__file__).with_name('settings.py')


class EnvironmentSettingsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from django.conf import settings

        # Standalone unittest needs defaults for HttpRequest, not project startup.
        if not settings.configured:
            settings.configure()

    def load(self, **values):
        # Clear ambient configuration so tests cannot use real credentials.
        with patch.dict(os.environ, values, clear=True):
            return runpy.run_path(str(SETTINGS))

    def production(self, **changes):
        values = {
            'DJANGO_SECRET_KEY': 'synthetic-test-only-key',
            'DJANGO_ALLOWED_HOSTS': 'tasks.example.test',
            'DB_NAME': 'synthetic',
            'DB_USER': 'synthetic',
            'DB_PASSWORD': 'synthetic-test-only-password',
            'DB_HOST': 'db.example.test',
        }
        values.update(changes)
        return values

    def test_missing_key_fails_without_fallback(self):
        with self.assertRaisesRegex(ImproperlyConfigured, 'DJANGO_SECRET_KEY'):
            self.load()

    def test_missing_or_blank_production_values_fail_without_echoing_secrets(self):
        base = self.production()
        for name in base:
            for replacement in (None, '', '   '):
                with self.subTest(name=name, replacement=replacement):
                    values = dict(base)
                    if replacement is None:
                        del values[name]
                    else:
                        values[name] = replacement
                    with self.assertRaises(ImproperlyConfigured) as error:
                        self.load(**values)
                    self.assertIn(name, str(error.exception))
                    self.assertNotIn(base['DJANGO_SECRET_KEY'], str(error.exception))
                    self.assertNotIn(base['DB_PASSWORD'], str(error.exception))

    def test_production_is_default_and_debug_defaults_false(self):
        result = self.load(**self.production())
        self.assertEqual(result['ENVIRONMENT'], 'production')
        self.assertIs(result['DEBUG'], False)
        self.assertEqual(result['SECRET_KEY'], 'synthetic-test-only-key')

    def test_explicit_production_rejects_debug_true(self):
        with self.assertRaisesRegex(ImproperlyConfigured, 'DJANGO_DEBUG'):
            self.load(**self.production(DJANGO_ENV='production', DJANGO_DEBUG='true'))

    def test_implicit_production_rejects_debug_true(self):
        with self.assertRaisesRegex(ImproperlyConfigured, 'DJANGO_DEBUG'):
            self.load(**self.production(DJANGO_DEBUG='true'))

    def test_boolean_parsing_and_invalid_values(self):
        for value, expected in [('false', False), ('FALSE', False), (' true ', True)]:
            with self.subTest(value=value):
                result = self.load(DJANGO_ENV='development', DJANGO_SECRET_KEY='synthetic',
                                   DJANGO_DEBUG=value)
                self.assertIs(result['DEBUG'], expected)
        for value in ('', '0', '1', 'yes', 'flase'):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ImproperlyConfigured, 'DJANGO_DEBUG'):
                    self.load(**self.production(DJANGO_DEBUG=value))

    def test_unknown_environment_fails_closed(self):
        for mode in ('', 'prodution', 'staging'):
            with self.subTest(mode=mode):
                with self.assertRaisesRegex(ImproperlyConfigured, 'DJANGO_ENV'):
                    self.load(**self.production(DJANGO_ENV=mode))

    def test_hosts_are_split_trimmed_and_enforced_by_django(self):
        result = self.load(**self.production(
            DJANGO_ALLOWED_HOSTS=' tasks.example.test, second.example.test, ,'
        ))
        self.assertEqual(result['ALLOWED_HOSTS'], ['tasks.example.test', 'second.example.test'])
        with override_settings(ALLOWED_HOSTS=result['ALLOWED_HOSTS'], DEBUG=False):
            request = HttpRequest()
            request.META['HTTP_HOST'] = 'tasks.example.test'
            self.assertEqual(request.get_host(), 'tasks.example.test')
            request.META['HTTP_HOST'] = 'untrusted.example.test'
            with self.assertRaises(DisallowedHost):
                request.get_host()

    def test_wildcard_hosts_rejected_in_production(self):
        with self.assertRaisesRegex(ImproperlyConfigured, 'DJANGO_ALLOWED_HOSTS'):
            self.load(**self.production(DJANGO_ALLOWED_HOSTS='tasks.example.test,*'))

    def test_postgresql_mapping_and_port_override(self):
        for port in (None, '6432'):
            with self.subTest(port=port):
                values = self.production(DB_ENGINE='postgresql')
                if port is not None:
                    values['DB_PORT'] = port
                db = self.load(**values)['DATABASES']['default']
                self.assertEqual(db, {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': values['DB_NAME'], 'USER': values['DB_USER'],
                    'PASSWORD': values['DB_PASSWORD'], 'HOST': values['DB_HOST'],
                    'PORT': port or '5432',
                })

    def test_invalid_postgresql_port_fails(self):
        for port in ('', 'wrong', '0', '65536'):
            with self.subTest(port=port):
                with self.assertRaisesRegex(ImproperlyConfigured, 'DB_PORT'):
                    self.load(**self.production(DB_PORT=port))

    def test_sqlite_only_available_in_development(self):
        result = self.load(DJANGO_ENV='development', DJANGO_SECRET_KEY='synthetic')
        self.assertIs(result['DEBUG'], False)
        self.assertEqual(result['DATABASES']['default']['NAME'], SETTINGS.parent.parent / 'db.sqlite3')
        result = self.load(DJANGO_ENV='development', DJANGO_SECRET_KEY='synthetic',
                           DB_ENGINE='sqlite3', DB_NAME=':memory:')
        self.assertEqual(result['DATABASES']['default']['NAME'], ':memory:')
        for engine in ('sqlite3', 'mysql', ''):
            with self.subTest(engine=engine):
                with self.assertRaisesRegex(ImproperlyConfigured, 'DB_ENGINE'):
                    self.load(**self.production(DB_ENGINE=engine))

    def test_development_postgresql_still_requires_password(self):
        with self.assertRaisesRegex(ImproperlyConfigured, 'DB_PASSWORD'):
            self.load(**self.production(DJANGO_ENV='development', DB_ENGINE='postgresql',
                                        DB_PASSWORD=''))


if __name__ == '__main__':
    unittest.main()
