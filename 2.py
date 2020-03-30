# Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
# екран значення коріння і квадратів кожного з елементів масиву.
# Гевчук Максим група 122А

import numpy as np

arr = np.zeros(5, dtype=int)
for i in range(5):
    arr[i] = int(input(f'Елемент {i + 1} >>> '))
for j in range(5):
    print(f'\nКорінь {arr[j]} = {np.sqrt(arr[j]):.2f}\n'
          f'Квадрат {arr[j]} = {arr[j] ** 2}')
