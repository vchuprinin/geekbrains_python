from requests import get

# 1
response = get(
    'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
with open('file.csv', 'w', encoding='utf-8') as f:
    f.write(response)

with open('file.csv', 'r+', encoding='utf-8') as f:
    data_list = [(line.split(' ')[0], line.split(' ')[5].split('"')[1], line.split(' ')[6]) for line in f.readlines()]

print(data_list)
print(len(data_list))  # 51462 - совпадает с кол строк
print('*' * 50)

# 2
ip_list = [data_list[i][0] for i in range(len(data_list))]
max_count = max(ip_list.count(i) for i in ip_list)
spammer = {(ip_list[i], max_count) for i in range(len(ip_list)) if ip_list.count(ip_list[i]) == max_count}

print(*spammer) # ('216.46.173.126', 2350)
print('*' * 50)

# 3
with open('users.csv', 'r+', encoding='utf-8') as f:
    user = [line.split('\n')[0] for line in f.readlines()]

with open('hobby.csv', 'r+', encoding='utf-8') as f:
    hobby = [line.split('\n')[0] for line in f.readlines()]

user_hobby = {}
with open('user_hobby.txt', 'w', encoding='utf-8') as f:
    for i in range(len(user)):
        user_hobby.setdefault(user[i], hobby[i])
    f.write(str(user_hobby))

# 4
with open('users.csv', 'r+', encoding='utf-8') as f:
    user = [line.split('\n')[0] for line in f.readlines()]

with open('hobby.csv', 'r+', encoding='utf-8') as f:
    hobby = [line.split('\n')[0] for line in f.readlines()]

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    f.writelines(((f'{user[i]}: {hobby[i]}\n') for i in range(len(user))))


# 5
def open_one_file(name):
    with open(name, 'r+', encoding='utf-8') as f:
        return [line.split('\n')[0] for line in f.readlines()]


one_file = open_one_file(input('Первый файл, например users.csv - '))


def open_two_file(name):
    with open(name, 'r+', encoding='utf-8') as f:
        return [line.split('\n')[0] for line in f.readlines()]


two_file = open_two_file(input('Второй файл, например hobby.csv - '))


def write_new_file(new_name):
    with open(new_name, 'w', encoding='utf-8') as f:
        f.writelines(
            ((f'{one_file[i]}: {two_file[i]}\n') for i in range(len(one_file))))
    print(f'Файл {new_name} успешно записан!')


if __name__ == '__main__':
    write_new_file(input('Новый файл, например user_hobby_2.txt - '))


