from unittest.mock import patch, MagicMock

from django.core.management import call_command
from django.db.utils import OperationalError # noqa
from django.test import SimpleTestCase


@patch('django.db.connections')
class CommandTests(SimpleTestCase):
    def test_wait_for_db_ready(self, patched_conn):
        mock_conn = MagicMock()
        patched_conn.__getitem__.return_value = mock_conn
        mock_conn.ensure_connection.return_value = True

        call_command('wait_for_db')

        mock_conn.ensure_connection.assert_called_once()

    # @patch('time.sleep')
    # def test_wait_for_db_delay(self, patched_sleep, patched_conn):
    #     mock_conn = MagicMock()
    #     patched_conn.__getitem__.return_value = mock_conn
    #     mock_conn.ensure_connection.side_effect = [OperationalError] * 3 /
    #     + [True]

    #     call_command('wait_for_db')

    #     self.assertEqual(mock_conn.ensure_connection.call_count, 1)
