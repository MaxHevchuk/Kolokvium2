# 39. Дані про температуру повітря і кількості опадів за декаду квітня зберігаються в масивах.
# Визначити кількість опадів, що випали у вигляді дощу і у вигляді снігу за цю декаду.
# Гевчук Максим КН-А

data = []
count_rain, count_snow = 0, 0
print('Введіть температуру повітря та к-сть опадів через пробіл: ')
for i in range(10):
    data.append(input(f'{i + 1}. ').split())  # до загального списку додається список типу ['0' , '10']
    data[i][0], data[i][1] = float(data[i][0]), float(data[i][1])  # перетворення елементів підсписку в числа

    if data[i][0] <= 0:
        count_snow += data[i][1]
    else:
        count_rain += data[i][1]
print(f'\nК-сть опадів:\n'
      f'- у вигляді дощу:  {count_rain}\n'
      f'- к вигляді снігу: {count_snow}')  # виведення
