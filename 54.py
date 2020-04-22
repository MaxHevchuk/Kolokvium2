# 54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з однаковими значеннями.
# Гевчук Максим КН-А

from random import randint

arr = [randint(1, 20) for i in range(20)]  # створення масиву
dict_arr = {x: arr.count(x) for x in set(arr)}  # створення словника із числа та скільки разів воно зустрічається
# виведення
print(*arr)
for k, v in zip(dict_arr.keys(), dict_arr.values()):
    print(f'Число {k}: к-сть {v}')
