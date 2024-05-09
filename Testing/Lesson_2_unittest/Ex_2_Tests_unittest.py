from Ex_2_unittest import is_prime
import unittest


class TestIsPrime(unittest.TestCase):
    def test_negative_number(self):
        self.assertRaises(ValueError, is_prime, -1)

    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_small_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(16))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(20))

    def test_large_prime_numbers(self):
        self.assertTrue(is_prime(997))
        self.assertTrue(is_prime(991))
        self.assertTrue(is_prime(983))
        self.assertTrue(is_prime(977))


if __name__ == '__main__':
    unittest.main()