from itertools import islice


# 1
def get_gen(num):
    yield (x for x in range(1, num, 2))


print(*next(get_gen(15)), sep=',')
print('*' * 50)


# 2
def get_gen_2(num):
    get_gen_slice = (x for x in range(0, num + 1, 2))
    print(*islice(get_gen_slice, 3))


get_gen_2(15)
print('*' * 50)

# 3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

klasses = klasses + [klasses.append(None) for i in range(len(tutors)) if len(tutors) > len(klasses)]
gen_tuple = ((tutors[i], klasses[i]) for i in range(len(tutors)))

print(*gen_tuple)
print('*' * 50)

# 4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
number = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]

print(number)
print('*' * 50)

# 5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
number = [num for num in src if src.count(num) == 1]

print(number)
