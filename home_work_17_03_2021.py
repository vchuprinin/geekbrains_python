import re

# 1
regular = re.compile(r'([a-z]+)\@([a-z]+[.][a-z]+)')


def email_parse(text):
    user, domain, user_dict = [], [], {}
    for i in range(len(regular.findall(text))):
        user.append(regular.findall(text)[i][0])
        domain.append(regular.findall(text)[i][1])
        user_dict.setdefault('user_name', user)
        user_dict.setdefault('domain', domain)
    return user_dict


print(email_parse('бла бла бла info@mail.ru и мы ответим @ вам с inin@gmail.com'))


# 3
def type_logger(func):
    def wrapper(*args):
        result = func(*args)
        print(f'{", ".join(map(str, args))}: {type(*args)}')
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(2))


# 4
def val_checker(callback):
    def _logger(func):
        def wrapper(*args):
            result = func(*args)
            msg = f'\tcall  {func.__name__} '
            msg = f' {msg} ->  {result} '
            return msg

        return wrapper

    return _logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    if x > 0:
        return x ** 3
    else:
        return f'ValueError: wrong val {x}'


print(calc_cube(-5))
