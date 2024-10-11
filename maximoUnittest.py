import unittest
import math as m


def square_integer(num):
    if isinstance (num, int):
        return m.pow(num, 2)
    else: 
        return "Please enter a valid integer:"

class TestFunction(unittest.TestCase):

    def test_square_integer(self):
        result = square_integer(5)
        self.assertEqual(result, 25)

    def  test_square_integer_negative(self):
        result = square_integer(-4)
        self.assertEqual(result, 16)

    def test_integer_valid(self):
        result = square_integer(2.5)
        self.assertEqual(result, "Please enter a valid integer:")

if __name__ == "__main__":
    unittest.main()