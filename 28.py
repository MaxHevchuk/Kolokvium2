# 28. Знайти кількість парних елементів одновимірного масиву.
# Гевчук Максим КН-А

arr = list(map(int, input('Введіть елементи масиву:\n>>> ').split()))  # введення елементів
print(f'Кількість парних елементів: {len(list(filter(lambda x: x % 2 == 0, arr)))}')  # виведення
