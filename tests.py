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
        self.assertEquals('102', format_price(price))

    def test_correct_float_with_zer_after_point(self):
        price = 101.0009
        self.assertEquals('101', format_price(price))

    def test_only_zero(self):
        price = 000000000.0000000
        self.assertEqual('0', format_price(price))

    def test_correct_small_float(self):
        price = 00000.009
        self.assertEqual('0.01', format_price(price))

    def test_incorrect_exponential_number(self):
        price = 1.234568e+04
        self.assertEqual('12 345.68', format_price(price))

    def test_incorrect_string(self):
        self.assertEquals(None, format_price('qwerty'))

    def test_incorrect_string_number_with_comma(self):
        self.assertEquals(None, format_price('55,56'))

    def test_incorrect_string_number_with_space(self):
        self.assertEquals(None, format_price('55 56'))

    def test_incorrect_tuple_of_numbers(self):
        self.assertEquals(None, format_price((55, 56)))

    def test_incorrect_string_with_digit(self):
        self.assertEquals(None, format_price('rhr123qwbey.4r58ty'))

    def test_incorrect_list_of_number(self):
        self.assertEquals(None, format_price([101.99]))

    def test_incorrect_list_of_string(self):
        self.assertEquals(None, format_price(['101.99']))

    def test_incorrect_dict(self):
        self.assertEquals(None, format_price({'number': 101.50}))

    def test_incorrect_boolean_value(self):
        self.assertEqual(None, format_price(True))

    def test_incorrect_complex_number(self):
        self.assertEqual(None, format_price(complex(3, 4)))


if __name__ == '__main__':
    unittest.main()
