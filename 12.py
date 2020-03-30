# 12. Дані про температуру повітря за декаду грудня зберігаються в масиві.
# Визначити, скільки раз температура була вище середньої за цю декаду.
# Гевчук Максим КН-А
from numpy import average

arr = tuple(map(float, input('Введіть масив даних про температуру через пробіл:\n>>> ').split()))
average_t = average(arr)
cound_t = len(tuple(filter(lambda x: x > average_t, arr)))
print(f'Середня температура {average_t}°\n'
      f'{cound_t} разів температура була вище середньої')
