"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import random
from timeit import timeit


def median_search(lst_obj):
    for idx in range(len(lst_obj) // 2):
        lst_obj.remove(max(lst_obj))
        return max(lst_obj)


m = int(input('Введите число m: '))
my_list = [random.randint(0, 100) for idx in range(2 * m + 1)]
print(my_list)
print(median_search(my_list))
print(timeit('median_search(my_list.copy())',
             setup='from __main__ import median_search, my_list',
             number=100))
