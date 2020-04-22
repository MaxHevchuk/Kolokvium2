# 25. Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5. Розмірність масиву - 10.
# Заповнення масиву здійснити випадковими числами від 10 до 100.
# Гевчук Максим КН-А

from random import randint
from numpy import prod

arr = [randint(10, 100) for i in range(10)]  # створення масиву
total = prod(list(filter(lambda x: x % 5 == 0, arr)))  # фільтр та сума чисел, які кратні 5
# виведення
print(*arr)
print(f'Добуток: {total}')