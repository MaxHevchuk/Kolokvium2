# Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в  один рядок через кому.
# Отримайте для масиву середнє арифметичне.
# Гевчук Максим КН-А

arr = []
for i in range(5):
    arr.append(int(input(f'Елемент {i + 1} >>> ')))  # вводяться елементи в цей масив
print(f"\n{', '.join((map(str, arr)))}")  # вивід елементів в один рядок
print(f'Середнє арифметичне = {sum(arr)/len(arr)}')  # вивід середнього арифметичного елементів масиву