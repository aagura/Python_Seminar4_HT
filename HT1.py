# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random
max_rand = 20
lenth_array_1 = int(input ("Введите длину массива 1: "))
lenth_array_2 = int(input ("Введите длину массива 2: "))
array_1 = [random.randrange(1, max_rand, 1) for i in range(lenth_array_1)]
array_2 = [random.randrange(1, max_rand, 1) for i in range(lenth_array_2)]
print(array_1)
print(array_2)
print (sorted(set(array_1).intersection(set(array_2))))
