# 36. Знайти суму додатніх елементів лінійного масиву цілих чисел.
# Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
# Гевчук Максим КН-А

arr = [int(input(f'{i+1}-ий елемент: ')) for i in range(10)]
total = sum(tuple(filter(lambda x: x > 0, arr)))
print(f'Сума додатніх елементів масиву: {total}')