"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""


import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if i % 2 == 0]


numbers = [i for i in range(10)]

print(timeit.timeit('func_1(numbers)', setup="from __main__ import func_1, numbers", number=1000))
print(timeit.timeit('func_2(numbers)', setup='from __main__ import func_2, numbers', number=1000))

"""
Генератор работает быстрее создания списка через цикл 
"""
