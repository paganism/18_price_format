import re
import argparse


def get_price():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--price',
        dest='price',
        help='This is the price'
    )
    return parser.parse_args()


def format_price(price):
    if isinstance(price, (int, float)):
        return "{0:.2f}".format(price)
    elif re.search('\d+[.,]?\d', price):
        return "{0:.2f}".format(float(price.replace(',', '.')))
    else:
        raise ValueError('Incorrect Value')


if __name__ == '__main__':
    price = get_price()
    print(format_price(price.price))
