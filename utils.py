from requests import get, utils
from datetime import datetime


def currency_rates(key):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings).split('<')
    date_content = content[2].split('"')[1].split('.')

    currency_filter, price_filter, currency_dict = [], [], {}
    currency_filter.append(list(filter(lambda x: x.startswith('CharCode>'), content)))
    price_filter.append(list(filter(lambda x: x.startswith('Value>'), content)))

    for i in range(len(currency_filter[0])):
        currency_dict.setdefault(currency_filter[0][i][9:], float(price_filter[0][i][6:].replace(',', '.')))

    return currency_dict.get(str(key).upper()), str(datetime(year=int(date_content[2]),
                                                             month=int(date_content[1]),
                                                             day=int(date_content[0])).date())


if __name__ == '__main__':
    print(*currency_rates('usd'))
