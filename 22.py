# 22. Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
# Заповнення масиву здійснити випадковими числами від 5 до 500.
# Гевчук Максим КН-А

from random import randint
from numpy import prod

arr = [randint(5, 500) for i in range(10)]  # створення масиву
product = prod(list(filter(lambda x: x % 3 == 0 and x % 9 == 0, arr)))  # фільтр та добуток елементів за умовою
# виведення
print(*arr)
print(f'Добуток: {product}')
