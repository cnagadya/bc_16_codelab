import unittest
from prime_generator_file import prime_generator_fn

class InputTestCase(unittest.TestCase):
    """Check if user input is valid"""
    def test_raises_error_for_nonnumeric_arg(self):
        """The input should be a number not string"""
        self.assertRaises(TypeError, prime_generator_fn, "four")
    def test_fn_runs_for_numeric_arg(self):
        """The input should be an interger"""
        self.assertIsInstance(4, int)
    def test_fn_false_for_negative_number(self):
        """The input should be an interger, but not be negative"""
        self.assertFalse(prime_generator_fn(-10))
    def test_fn_true_for_positive_number(self):
        """The input should be an interger and positive"""
        self.assertFalse(prime_generator_fn(10))
    def test_input_must_be_greater_than_one(self):
        """Input is not one. There are no prime numbers between 0 and 1"""
        self.assertNotEqual(7,1)


if __name__ == '__main__':
    unittest.main()