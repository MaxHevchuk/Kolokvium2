# 16. Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
# масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
# Гевчук Максим КН-А

from random import randint
from numpy import prod

arr = [randint(10, 50) for i in range(15)]
total = prod(tuple(filter(lambda x: x % 7 == 0, arr)))
print(f'Масив елементів:\n{arr}\n'
      f'Добуток елементів, які кратні 7:\n{total}')
