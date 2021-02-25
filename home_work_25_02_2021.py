# 1.
print(type(15 * 3))  # <class 'int'>
print(type(15 / 3))  # <class 'float'>
print(type(15 // 2))  # <class 'int'>
print(type(15 ** 2))  # <class 'int'>
print('*_' * 50)

# 2-3.
one_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
one_list.insert(1, '05')
one_list.insert(9, '+05')
one_list.remove('5')
one_list.remove('+5')
one_list.insert(1, '"')
one_list.insert(3, '"')
one_list.insert(5, '"')
one_list.insert(7, '"')
one_list.insert(12, '"')
one_list.insert(14, '"')
one_list = ' '.join(one_list) # <class 'str'>
print(one_list)

one_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print('в "{0:02d}" часов "{1}" минут температура воздуха была "+{2:02d}" градусов'.format(int(one_list[1]), int(one_list[3]), int(one_list[-2])))

# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# поможет конструкция try: except, в цикле, но мы их еще не проходили
print('*_' * 50)

# 4.
personal = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(personal)):
    personal[i] = personal[i].title()
    personal[i] = personal[i].split(' ')
    print('Привет,', personal[i][-1])
print('*_' * 50)

# 5.A-B
price_list = [10, 24.5, 34.09, 9.99, 48.67, 4, 11.56, 104, 0.99, 61.7] #id 4504950976
price_list.sort() #id 4504950976
rub_str = ' руб '
cent_str = ' коп '
for i in range(len(price_list)):
    if type(price_list[i]) == int:
        price_list[i] = float(price_list[i])
    if type(price_list[i]) == float:
        price_list[i] = format(price_list[i], '.2f')
        price_list[i] = str(price_list[i]).split('.')
        price_list[i][0] = price_list[i][0] + rub_str
        price_list[i][1] = price_list[i][1] + cent_str
        price_list[i] = ''.join(price_list[i])
price_list = ', '.join(price_list)
print(price_list)

# 5.C-D
price_list = [10, 24.5, 34.09, 9.99, 48.67, 4, 11.56, 104, 0.99, 61.7] #id 4475828480
price_list.sort(reverse=True)
print(price_list)
print(price_list[:5])




