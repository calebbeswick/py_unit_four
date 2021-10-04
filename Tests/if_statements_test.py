import unittest
from even_odd import even_or_odd
from abs_value import absolute_value
from maximum import biggest_number


class MyTestCase(unittest.TestCase):
    def test_bonus(self):
        self.assertEqual(5, absolute_value(-5))
        self.assertEqual(5, absolute_value(5))
        self.assertEqual(10, absolute_value(10))

    def test_max(self):
        self.assertEqual(10, biggest_number(10, 5))
        self.assertEqual(10, biggest_number(5, 10))
        self.assertEqual(10, biggest_number(-5, 10))
        self.assertEqual(-10, biggest_number(-5, -10))





    # In the space below, write a test function for bonus. Make sure to import the appropriate information
    # at the top of this file. Make sure to write three test cases.



if __name__ == '__main__':
    unittest.main()
