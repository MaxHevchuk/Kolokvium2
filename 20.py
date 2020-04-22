# 20. Знайти суму всіх елементів масиву дійсних чисел, більших за задане число. Розмірність масиву - 20.
# Заповнення масиву здійснити випадковими числами від 50 до 100.
# Гевчук Максим КН-А

from random import randint

arr = [randint(50, 100) for i in range(20)]  # створення масиву із рандомними елементами
num = int(input('Введіть число:\n>>> '))  # введення числа
total = sum(tuple(filter(lambda x: x > num, arr)))  # фільтр та сума елементів, що більше за задане число
print(f'Масив елементів:\n{arr}\n'  # виведення
      f'Сума елементів, які більші за {num}:\n{total}')
