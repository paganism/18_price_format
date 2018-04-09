import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):
    def test_correct_int(self):
        price = 101
        self.assertEquals('101.00', format_price(price))

    def test_correct_float(self):
        price = 101.9999
        self.assertEquals('102.00', format_price(price))

    def test_correct_negative_float(self):
        price = -101.9999
        self.assertEquals('-102.00', format_price(price))

    def test_correct_string(self):
        price = '101.9999'
        self.assertEquals('102.00', format_price(price))

    def test_correct_string_with_comma(self):
        price = '101,9999'
        self.assertEquals('102.00', format_price(price))

    def test_correct_string_with_spaces(self):
        price = '   101.9999   '
        self.assertEquals('102.00', format_price(price))

    def test_incorrect_string(self):
        with self.assertRaises(ValueError):
            format_price('qwerty')

    def test_incorrect_string_with_digit(self):
        with self.assertRaises(ValueError):
            format_price('123qwbey.4r58ty')


if __name__ == '__main__':
    unittest.main()
