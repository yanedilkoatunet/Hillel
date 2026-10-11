
import unittest
from unittest.mock import patch
from lesson_13.homework_13 import log_event


class TestLogEvent(unittest.TestCase):

    @patch("lesson_13.homework_13.logging.getLogger")
    def test_success(self, mock_logger):
        log_event("Liza", "success")

        mock_logger.return_value.info.assert_called_once_with(
            "Login event - Username: Liza, Status: success"
        )

    @patch("lesson_13.homework_13.logging.getLogger")
    def test_expired(self, mock_logger):
        log_event("Liza", "expired")

        mock_logger.return_value.warning.assert_called_once_with(
            "Login event - Username: Liza, Status: expired"
        )

    @patch("lesson_13.homework_13.logging.getLogger")
    def test_failed(self, mock_logger):
        log_event("Liza", "failed")

        mock_logger.return_value.error.assert_called_once_with(
            "Login event - Username: Liza, Status: failed"
        )


if __name__ == "__main__":
    unittest.main()
