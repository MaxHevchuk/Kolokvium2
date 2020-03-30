# 12. Дані про температуру повітря за декаду грудня зберігаються в масиві.
# Визначити, скільки раз температура була вище середньої за цю декаду.
# Гевчук Максим КН-А
from numpy import mean

arr = tuple(map(float, input('Введіть масив даних про температуру через пробіл:\n>>> ').split()))  # ввидення даних
average_t = mean(arr)  # знаходження середньої температури
cound_t = len(tuple(filter(lambda x: x > average_t, arr)))  # фільтр та підрахунок темп., що вище середньої
print(f'Середня температура {average_t}°\n'  # виведення
      f'{cound_t} разів температура була вище середньої')  # виведення
