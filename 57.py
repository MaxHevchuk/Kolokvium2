# 57. Відомість на зарплату представлена як дві таблиці. Одна містить прізвища працівників цеху, а друга - їх зарплату
# за поточний місяць. Знайдіть прізвище працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
# працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою заробітною платою. Видаліть з
# відомості на зарплату відомості про працівника, зарплата якого мінімальна.
# Гевчук Максим КН-А

from copy import deepcopy as deep


def minimalDifference(av, sal, sur):
    """Функція обчисленя індекс зарплати, яка найменше відхиляється від середньої.

    Обчислюється як найменша різниця середньої та кожного з працівників зарплати по модулю"""

    last, min_diff, id_ = 0, max(sal), 0
    for s in sal:
        last = abs(av - s)
        if min_diff > last:
            id_ = sal.index(s)
            min_diff = last
            last = 0
    return id_


def highestSalary(sur, sal):
    """Функція обчислення індексів прізвищ двох працівників, у яких найбільша зарплата.

    У сортованому масиві-копії знаходяться індекси останніх елементів вхідного масиву"""

    return sal.index(sorted(sal)[-1]), sal.index(sorted(sal)[-2])


def smallestSalary(sur, sal):
    """Функція обчислення та видалення інформації про працівника з найменшою зарплатою.

    Знаходиться індекс мінімальної зарплати та за ним видаляється прізвище та його зарплата"""
    id_ = sal.index(min(sal))
    sur.pop(sal.index(min(sal)))
    sal.remove(min(sal))
    return id_, sur, sal


surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
salary = [8536, 9664, 9288, 7972, 8912, 7785, 8724, 10227, 8160, 9100]
average = sum(salary) / len(salary)

# результати функ. присвоюються змінним
task_1 = minimalDifference(average, salary, surnames)  # індекс
task_2 = highestSalary(surnames, salary)  # кортеж [індекс, індекс]
task_3 = smallestSalary(sur=deep(surnames), sal=deep(salary))  # кортеж [індекс, змінені прізвища, змінені зарплати]

print(f'\nПрізвища працівників та їхня зарплата до змін:\n{surnames}\n{salary}\n')

print(f'Середня зарплата працівників: {average}')
print(f'У {surnames[task_1]} зарплата відхиляється від середньої зарплати всіх працівників '
      f'та складає {salary[task_1]}')
print(f'Найбільша зарплата в {surnames[task_2[0]]} та {surnames[task_2[1]]},'
      f'яка складає {salary[task_2[0]]} та {salary[task_2[1]]} відповідно')
print(f'Найменша зарплата в {surnames[task_3[0]]}, яка складає {salary[task_3[0]]}\n')
print(f'Прізвища працівників та їхня зарплата до змін:\n{task_3[1]}\n{task_3[2]}')
