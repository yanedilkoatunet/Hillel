import unittest
from homeworks import (
    sum_numbers,
    average_numbers,
    reverse_string,
    find_substring,
    all_sum,
)


class TestSumNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_numbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(sum_numbers(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(sum_numbers(0, 5), 5)


class TestAverageNumbers(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average_numbers([2, 4, 6]), 4)

    def test_one_number(self):
        self.assertEqual(average_numbers([10]), 10)

    def test_float_result(self):
        self.assertEqual(average_numbers([1, 2]), 1.5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            average_numbers([])


class TestReverseString(unittest.TestCase):

    def test_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_one_character(self):
        self.assertEqual(reverse_string("a"), "a")


class TestFindSubstring(unittest.TestCase):

    def test_substring_exists(self):
        self.assertEqual(find_substring("hello world", "world"), 6)

    def test_substring_missing(self):
        self.assertEqual(find_substring("hello", "xyz"), -1)

    def test_substring_at_start(self):
        self.assertEqual(find_substring("hello", "he"), 0)

    def test_empty_substring(self):
        self.assertEqual(find_substring("hello", ""), 0)


class TestAllSum(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(all_sum("1,2,3,4"), 10)

    def test_large_number(self):
        self.assertEqual(all_sum("1,2,3,4,50"), 60)

    def test_negative_numbers(self):
        self.assertEqual(all_sum("10,-2,5"), 13)

    def test_invalid_string(self):
        self.assertEqual(
            all_sum("qwerty1,2,3"),
            "Не можу це зробити!"
        )

    def test_empty_element(self):
        self.assertEqual(
            all_sum("1,,3"),
            "Не можу це зробити!"
        )


if __name__ == "__main__":
    unittest.main()
