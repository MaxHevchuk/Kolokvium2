# 45. Перетин даху має форму півкола з радіусом R м. Сформувати таблицю, яка містить довжини опор,
# які встановлюються через кожні R / 5 м.
# Гевчук Максим КН-А


from math import sqrt

r = float(input('Введіть радіус кола:\n>>> '))
length, step = 0, r / 5
arr = []
for i in range(9):  # 9 - який би радіус не мало б коло, у нього буде 9 балок, відстань між якими r/5
    length += step
    arr.append(sqrt(length * (2 * r - length)))  # рахується довжина балки та додається у масив
for j in range(len(arr)):
    print(f'{j + 1} опора = {arr[j]}')