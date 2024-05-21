import pytest
from unittest.mock import patch
from write_log_message import write_log_message


def test_write_log_message():
    message = 'Hello, world!'
    with patch('builtins.open') as mock_open:
        write_log_message(message)
        mock_open.assert_called_once_with('log.txt', 'w')
        mock_open.return_value.__enter__.return_value.write.assert_called_once_with(message)


def test_write_log_message_error():
    with patch('builtins.open') as mock_open:
        mock_open.side_effect=FileNotFoundError('Error')
        with pytest.raises(FileNotFoundError):
            write_log_message('Test')
