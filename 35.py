# 35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
# спаданню.
# Гевчук Максим КН-А

arr = list(map(int, input("Введіть лінійний масив через пробіл:\n>>> ").split()))
print('Масив є упорядкованим за спаданням'
      if all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))  # if arr == sorted(arr, reverse=True)
      else 'Масив НЕ є упорядкованим за спаданням')