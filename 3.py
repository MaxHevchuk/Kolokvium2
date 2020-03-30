# 3. Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
# починаючи з останнього.
# Гевчук Максим група 122А

import numpy as np

surnames = np.array(['Smith', 'Johnson', 'Williams', 'Jones', 'Brown'])
for name in surnames[::-1]:
    print(name)
