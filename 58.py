# 58. Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому повторюється найчастіше число.
# Гевчук Максим КН-А

from random import randint

arr = [randint(0, 10) for i in range(int(input('Введіть розмір масиву:\n>>> ')))]  # створюється масив із чисел
tr = [arr.count(c) for c in set(arr)]  # рахується скільки разів повторюється кожне число і додається в масив
max_tr = max(tr)
print(*arr)
print(f'Число {list(set(arr))[tr.index(max_tr)]} повторюється {max_tr} разів' if max_tr != 1
      else 'Немає чисел, що повторюються')
