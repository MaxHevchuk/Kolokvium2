# 60. Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число однакових чисел, що йдуть підряд в ньому.
# Гевчук Максим КН-А

from random import randint

arr = [randint(1, 4) for i in range(10)]
last_num, num = 1, 1  # лічильники

for i in range(1, 10):
    # перебираються елементи, якщо число = попередньому, то last_num збульшується на 1
    if arr[i - 1] == arr[i]:
        last_num += 1
    # якщо числа не будуть однаковими, то last_num стає 1, а num = last_num, якщо last_num > num
    else:
        num = last_num if last_num > num else num
        last_num = 1
# остаточна перевірка на випадок, якщо однакові числа будуть знаходитись у кінці масиву
num = last_num if last_num > num else num
# виведення
print(*arr)
print(f'Найбільша кількість однакових чисел, що йдуть підряд:\n{num}')
