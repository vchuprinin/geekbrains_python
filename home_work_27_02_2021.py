from random import choice


# 1
print('*' * 50, '№1\n')
num = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
       'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(key):
    return num.get(key)


print(num_translate('zero'), '\n')  # None

# 2
print('*' * 50, '№2\n')


def num_translate_adv(key):
    """
    'NoneType' object has no attribute 'title'
    :param key: 'one' <= str <= 'ten'
    :return: str
    """
    if num.get(key) == None:
        key = key.lower()
        return num.get(key).title()
    else:
        return num.get(key)


print(num_translate_adv('Nine'), '\n')

# 3
print('*' * 50, '№3\n')


def thesaurus(*args):
    user_dict = {}
    for i in range(len(args)):
        user_list = []
        user_list.extend(list(filter(lambda x: x.startswith(args[i][:1]), args)))
        user_dict.setdefault(args[i][:1], user_list)
    return user_dict


print(thesaurus('Ангелина', 'Юлия', 'Полина', 'Аксиния', 'Юрий'), '\n')

# 4
print('*' * 50, '№4\n')

# 5
print('*' * 50, '№5\n')
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    """
    funny function 😄
    :param num: int
    :return: None
    """
    for i in range(1, (num + 1)):
        print(f'"{choice(nouns).title()} {choice(adverbs)} {choice(adjectives)}"')


get_jokes(2)
help(get_jokes)
