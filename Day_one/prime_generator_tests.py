import unittest
from prime_generator_file import prime_generator_fn

class InputTestCase(unittest.TestCase):
    """Check if user input is valid"""
    def test_is_only_one_arg(self):
        """The input should only be one value"""
        self.assertRaises(ERROR, n, 3, args)
    def test_is_int(self):
        """Is the input an interger"""
        self.assertIsInstance(n, int)
    def test_is_negative_int(self):
        """Input should not be negative"""
        self.assertFalse(-10)
    def test_is_positibe_int(self):
        """Is the input a positive number?"""
        self.assertTrue(10)
    def test_is_1(self):
        """Prime numbers need to be greater than one"""
        self.assertEqual(n,1)


if __name__ == '__main__':
    unittest.main()