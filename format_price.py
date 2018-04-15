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
    if (isinstance(price, (int, float)) and
            not isinstance(price, bool)) or (
                isinstance(price, str) and
                re.search('(^\d+(\.\d+)$)|^\d*$', price)):
        price = float(price)
        if round(price, 2) % 1 == 0:
            return format(price, ',.0f').replace(',', ' ')
        else:
            return format(price, ',.2f').replace(',', ' ')
    else:
        return None


if __name__ == '__main__':
    args = parse_arguments()
    price = args.price
    print(format_price(price))
