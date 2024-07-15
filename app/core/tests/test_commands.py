from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('django.db.backends.postgresql.base.DatabaseWrapper.ensure_connection')
class CommandTests(SimpleTestCase):

    def test_wait_for_db_ready(self, patched_conn):
        patched_conn.return_value = True

        call_command('wait_for_db')

        patched_conn.assert_called_once()

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_conn):
        patched_conn.side_effect = [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_conn.call_count, 4)
