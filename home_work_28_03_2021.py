from abc import ABC, abstractmethod


num_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
num_list2 = [[12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        new_list = []
        for i in range(len(self.list)):
            new_list.append([])
            for j in range(len(self.list[0])):
                new_list[i].append(self.list[i][j] + other.list[i][j])
        return '\n'.join(map(str, new_list)).replace(',', '').replace('[', '').replace(']', '')

mayrix_1 = Matrix(num_list)
mayrix_2 = Matrix(num_list2)

print(mayrix_1 + mayrix_2)


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f'{res}'

class Coat(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param / 6.5) + 0.5)


class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)

coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)


    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Sum of cell is:')
        return Cell(self.nums + other.nums)
