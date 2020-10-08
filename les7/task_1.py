"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for idx in range(len(lst_obj) - n):
            if lst_obj[idx] > lst_obj[idx + 1]:
                lst_obj[idx], lst_obj[idx + 1] = lst_obj[idx + 1], lst_obj[idx]

        n += 1
    return lst_obj


def bubble_sort2(lst_obj):
    n = 1
    flag = 0
    while n < len(lst_obj):
        for idx in range(len(lst_obj) - n):
            if lst_obj[idx] < lst_obj[idx + 1]:
                lst_obj[idx], lst_obj[idx + 1] = lst_obj[idx + 1], lst_obj[idx]
                flag = 1
        if flag == 0:
            break
        n += 1
    return lst_obj


my_list = [random.randint(-100, 100) for el in range(10)]
print(my_list)
print(bubble_sort(my_list))
print(bubble_sort2(my_list))

print(timeit('bubble_sort(my_list.copy())',
             setup='from __main__ import bubble_sort, my_list',
             number=100))
print(timeit('bubble_sort2(my_list.copy())',
             setup='from __main__ import bubble_sort2, my_list',
             number=100))

