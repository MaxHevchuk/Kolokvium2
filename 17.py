# 17. Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
# Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100 до 200.
# Гевчук Максим КН-А

from random import randint

arr = [randint(100, 200) for i in range(20)]  # створення масиву із рандомними елементами
print(f'Масив елементів:\n{arr}\n'  # виведення
      f'Сума елементів з непарними індексами:\n{sum(arr[1::2])}')
