# 3. Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
# починаючи з останнього.
# Гевчук Максим КН-А

surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown']  # створюється масив із прізвищ
for name in reversed(surnames):  # вивід прізвищ, починаючи з останнього
    print(name)
