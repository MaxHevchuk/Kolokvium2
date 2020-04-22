# 44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі своїм номером і при цьому кратні 3.
# Гевчук Максим КН-А

from random import randint

arr = [randint(0, 5) for i in
       range(int(input('Введіть довжину масиву:\n>>> ')))]  # створення масиву з рандомних елементів
numbers = list(set(
    filter(lambda x: arr.index(x) == x and x % 3 == 0, arr)))  # фільтр чисел, що задовільняють умову
print(f'Масив:\n{arr}')  # виведення
print(f'{len(numbers)} - к-сть чисел, що задовільняють умову; це{numbers}' if numbers else
      f'Такий чисел немає')
