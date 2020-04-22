# 23. Знайти суму всіх елементів масиву цілих чисел, які менше середнього арифметичного елементів масиву.
# Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 150 до 300.
# Гевчук Максим КН-А

from random import randint

arr = [randint(150, 300) for i in range(20)]  # створення масиву
average = sum(arr)/len(arr)  # підрахунок середнього арифметичного
result = sum(list(filter(lambda x: x < average, arr)))  # фільтр та сума чисел, які менші середнього арифметичного
# виведення
print(*arr)
print(f'Середнє арифметичне: {average}')
print(f'Сума: {result}')
