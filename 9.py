# 9. З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
# що протягом цього часу температура знижувалася. Визначте, о котрій годині було
# вперше зафіксовано від'ємну температуру.
# Гевчук Максим КН-А
arr = []
for i in range(13):
    arr.append(float(input(f'{i + 8}:00. ℃ = ')))
negative_T = 0
for temperature in arr:
    if temperature < 0:
        negative_T = temperature
        break
print(f'Вперше від\'ємну температуру було зафіксовано о {arr.index(negative_T) + 8} годині.')
