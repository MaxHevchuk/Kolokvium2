# 3. Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
# починаються з певної букви, яка вводиться з клавіатури.
# Гевчук Максим КН-А
import numpy as np

surnames = np.array(['Smith', 'Johnson', 'Williams', 'Jones', 'Brown'])
letter = input('Введіть букву:\n>>> ')

for name in surnames:
    if name[0] == letter:
        print(name)
