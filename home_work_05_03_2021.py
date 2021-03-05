import utils


def func_less(argv):
    currency_rates, key = argv
    print(*utils.currency_rates(key))


if __name__ == '__main__':
    import sys

    exit(func_less(sys.argv))
