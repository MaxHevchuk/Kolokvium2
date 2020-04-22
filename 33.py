# 33. Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
# Гевчук Максим КН-А

from numpy import prod
from random import randint

arr = [randint(0, 2) for i in range(20)]  # створення масиву
print(*arr)
print(f'Добуток: {prod(list(filter(lambda x: x != 0, arr)))}')  # виведення результату добутку
