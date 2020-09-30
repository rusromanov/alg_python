"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def time_meter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(args[0])
        print(f'Time result: {time.time() - start}')
    return wrapper


@time_meter
def time_list(n):
    user_list = list()
    for idx in range(n):
        user_list.append(idx)
        user_list.index(idx)
    return user_list


@time_meter
def time_dict(n):
    user_dict = dict()
    for idx in range(n):
        user_dict[idx] = idx
        user_dict.get(idx)
    return user_dict


time_meter(time_list(10000))
time_meter(time_dict(10000))
