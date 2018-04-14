import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):
    def test_correct_int(self):
        price = 101
        self.assertEquals('101', format_price(price))

    def test_correct_long_int(self):
        price = 123456789
        self.assertEquals('123 456 789', format_price(price))

    def test_correct_float(self):
        price = 101.116
        self.assertEquals('101.12', format_price(price))

    def test_correct_long_float(self):
        price = 123456789.114
        self.assertEquals('123 456 789.11', format_price(price))

    def test_correct_negative_float(self):
        price = -101.55
        self.assertEquals('-101.55', format_price(price))

    def test_correct_string(self):
        price = '101.9999'
        self.assertEquals('102.00', format_price(price))

    def test_incorrect_string(self):
        self.assertEquals(None, format_price('qwerty'))

    def test_incorrect_string_with_spaces(self):
        price = '     101.9999     '
        self.assertEquals(None, format_price(price))

    def test_incorrect_string_with_digit(self):
        self.assertEquals(None, format_price('rhr123qwbey.4r58ty'))

    def test_incorrect_list_of_number(self):
        self.assertEquals(None, format_price([101.99]))

    def test_incorrect_list_of_string(self):
        self.assertEquals(None, format_price(['101.99']))

    def test_incorrect_dict(self):
        self.assertEquals(None, format_price({'number': 101.50}))


if __name__ == '__main__':
    unittest.main()
