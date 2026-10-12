
import unittest
from lesson_13.homework_13 import log_event


class TestLogEvent(unittest.TestCase):

    def test_success(self):
        with self.assertLogs("log_event", level="INFO") as logs:
            log_event("Liza", "success")

        self.assertEqual(
            logs.records[0].getMessage(),
            "Login event - Username: Liza, Status: success"
        )
        self.assertEqual(logs.records[0].levelname, "INFO")

    def test_expired(self):
        with self.assertLogs("log_event", level="WARNING") as logs:
            log_event("Liza", "expired")

        self.assertEqual(
            logs.records[0].getMessage(),
            "Login event - Username: Liza, Status: expired"
        )
        self.assertEqual(logs.records[0].levelname, "WARNING")

    def test_failed(self):
        with self.assertLogs("log_event", level="ERROR") as logs:
            log_event("Liza", "failed")

        self.assertEqual(
            logs.records[0].getMessage(),
            "Login event - Username: Liza, Status: failed"
        )
        self.assertEqual(logs.records[0].levelname, "ERROR")


if __name__ == "__main__":
    unittest.main()
