# 37. Розсортуйте заданий лінійний масив по зростанню.
# Гевчук Максим КН-А

from random import randint

arr = [randint(-10, 10) for i in range(15)]  # створення масиву
print(f'Масив:\n{arr}')
arr.sort()  # сортування
print(f'Відсортований масив:\n{arr}')
