# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

N = int(input("Введите длину массива "))
X = int(input("Введите число, ,близкое которому надо найти "))
array = []
rang = 100
clouse = rang
friend = 0
for i in range (N):
     array.append (randint(0, rang-1))
     if abs (X-array [i]) < clouse :
          clouse = abs (X-array [i]) 
          friend = array [i]  
print (array) 
print('Число', friend , 'наиболее близко числу', X)   
    

