# 30. Обчислити середнє арифметичне значення тих елементів одновимірного масиву, які розташовані за першим по порядку
# мінімальним елементом.
# Гевчук Максим КН-А

arr = list(map(int, input('Введіть елементи масиву через пробіл:\n>>> ').split()))  # введення
arr = arr[arr.index(min(arr) + 1):]  # зріз масиву після першого мін. числа
print(f'Середнє арифм. чисел після першого мін. числа: {sum(arr) / len(arr)}')  # виведення