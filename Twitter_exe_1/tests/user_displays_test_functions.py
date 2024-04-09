import unittest
from Implementation import user_display


class TestFunctions(unittest.TestCase):

    def test_odd_number(self):
        # Test with even numbers
        self.assertEqual(user_display.calculate_space_between_two_nums(5, 1), 2)  # Expected result: (5 - 2) // 2 = 2
        self.assertEqual(user_display.calculate_space_between_two_nums(9, 3), 3)  # Expected result: (9 - 3) // 2 = 2

    def test_odd_numbers(self):
        # Test with an odd number
        with self.assertRaises(ValueError):
            user_display.calculate_space_between_two_nums(5, 2)  # This should raise a ValueError

    def test_count_odd_numbers(self):
        self.assertEqual(user_display.count_odd_numbers(5), 1)  # There are 1 odd numbers (3 ) up to 5 without 5

    def test_calculate_space_between_two_nums(self):
        self.assertEqual(user_display.calculate_space_between_two_nums(5, 2), 1)  # The space between 5-1 and 2 is 1

    def test_calculate_repeater_lines(self):
        self.assertEqual(user_display.calculate_repeater_lines(7, 3),
                         (2, 3))  # For 7 lines and 3 odd numbers, 2 lines repeat, with 1 additional line at first

    def test_triangle_display(self):
        # Test that the function runs without errors
        user_display.triangle_display(5, 5)
        # Add more specific tests if needed


if __name__ == '__main__':
    unittest.main()
