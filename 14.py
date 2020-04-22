# 14. Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
# пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
# Гевчук Максим КН-А

arr_t = range(1, 11)  # створення масиву із часом
arr_s = list(map(lambda x: round((9.8 * x ** 2) / 2, 1), arr_t))  # за формулою s=gt^2/2 знаходимо масив із відстанями
print(f'Масив, елементи якого є відстанями:\n{arr_s}')  # виведення
