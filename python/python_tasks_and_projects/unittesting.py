import unittest
from unittest.mock import patch
from functions import prime_number


# unittest
# Best practice is normally to have a separate unittest file.
# Used to test edge cases, error handling, input and output.
# Used to test smallest parts of software - eg separate scripts.
# Best practice to test a few of each: in other words, for error handling, try 3 different inputs that should return an error message to see
# if an error message is returned every time, because if it doesn't work each time, it has 'failed'.


class TestPrimeNumber(unittest.TestCase):  # TestCase is a set of conditions used to determine whether the function
                                          # being tested works the way it should.

    # General testing - testing what should happen when the user inputs prime or non-prime integers. Testing large and small integers.
    def test_small_prime(self):
        self.assertTrue(prime_number(2))
        self.assertTrue(prime_number(3))
        self.assertTrue(prime_number(5))

    def test_small_not_prime(self):
        self.assertFalse(prime_number(4))
        self.assertFalse(prime_number(6))
        self.assertFalse(prime_number(8))

    def test_large_prime(self):
        self.assertTrue(prime_number(10007))
        self.assertTrue(prime_number(11113))
        self.assertTrue(prime_number(99991))

    def test_large_not_prime(self):
        self.assertFalse(prime_number(10000))
        self.assertFalse(prime_number(55222))
        self.assertFalse(prime_number(99999))


# Edge testing = test the objects on the edge of your given parameters.
    def test_edge_cases(self):
        self.assertFalse(prime_number(0))  # assertFalse allows us to test what happens when the Boolean value  should return False.
        self.assertFalse(prime_number(1))
        self.assertFalse(prime_number(-5))

# Error handling = test to see if the error message appears when the user types anything other than an integer
#     def test_error_handling(self):


if __name__ == "__main__":
    unittest.main()