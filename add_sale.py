from datetime import datetime


def write_order(order):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(order)
        #f.writelines(f'{datetime.today().time().replace(microsecond=0)} - {order} руб.\n')


if __name__ == '__main__':
    write_order(f'{input()}\n')
