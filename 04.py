# 3. Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
# починаються з певної букви, яка вводиться з клавіатури.
# Гевчук Максим КН-А

surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown']  # створення масиву прізвищ
letter = input('Введіть букву:\n>>> ')  # введеня букви, з якої має починатись прізвища

for name in surnames:
    if name[0] == letter:  # якщо прізвище починається із заданої букви,
        print(name)        # то воно виводиться на екран
