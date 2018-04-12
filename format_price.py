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
    if isinstance(price, (int, float)) or isinstance(price, str) and re.search('\d+[.]?\d', price):
        price = float(price)
        return format(price, ',.0f').replace(',', ' ')
    else:
        raise ValueError('Incorrect Value')


if __name__ == '__main__':
    args = parse_arguments()
    price = args.price
    print(format_price(price))
