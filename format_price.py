import re
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--price',
        dest='price',
        help='This is the price'
    )
    return parser.parse_args()


def format_price(price):
    if not isinstance(price, bool):
        try:
            price = round(float(price), 2)
            if price.is_integer():
                return format(price, ',.0f').replace(',', ' ')
            else:
                return format(price, ',.2f').replace(',', ' ')
        except ValueError:
            return None


if __name__ == '__main__':
    args = parse_arguments()
    price = args.price
    print(format_price(price))
