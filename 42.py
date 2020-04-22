# 42. Підрахувати кількість елементів одновимірного масиву, для яких виконується нерівність i*i<ai<i!
# Гевчук Максим КН-А

from random import randint
from math import factorial as fact

arr = [randint(0, 200) for j in
       range(int(input('Введіть довжину масиву:\n>>> ')))]  # створення масиву із рандомних елементів

# фільтр та підрахунок чисел,які входять в проміжок i*i<a<i!
count = len(tuple(filter(lambda a: arr.index(a) ** 2 < a < fact(arr.index(a)), arr)))

print(f'Масив елементів:\n{arr}\n'  # виведення
      f'К-сть елементів, для яких виконується i*i<ai<i!:\n{count}')
