"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
import timeit


def list_append(num):
    some_list = list()
    for idx in range(num):
        some_list.append(idx)


def deque_append(num):
    some_deque = deque()
    for idx in range(num):
        some_deque.append(idx)


def list_insert(num):
    some_list = list()
    for idx in range(num):
        some_list.insert(0, idx)


def deque_appendleft(num):
    some_list = deque()
    for idx in range(num):
        some_list.appendleft(idx)


def list_pop(lst_range):
    for idx in range(len(lst_range)):
        a = lst_range.pop()


def deque_pop(lst_range):
    for idx in range(len(lst_range)):
        a = lst_range.pop()


def list_popleft(lst_range):
    for idx in range(len(lst_range)):
        a = lst_range.pop(0)


def deque_popleft(lst_range):
    for idx in range(len(lst_range)):
        a = lst_range.popleft()


my_list = [el for el in range(1000)]
my_deque = deque()
my_deque.extend(my_list)

print(timeit.timeit('list_append, my_list', setup='from __main__ import list_append, my_list', number=100000))
print(timeit.timeit('list_insert, my_list', setup='from __main__ import list_insert, my_list', number=100000))
print(timeit.timeit('list_pop, my_list', setup='from __main__ import list_pop, my_list', number=100000))
print(timeit.timeit('list_popleft, my_list', setup='from __main__ import list_popleft, my_list', number=100000))
print(timeit.timeit('deque_append, my_deque', setup='from __main__ import deque_append, my_deque', number=100000))
print(timeit.timeit('deque_appendleft, my_deque', setup='from __main__ import deque_appendleft, my_deque', number=100000))
print(timeit.timeit('deque_pop, my_deque', setup='from __main__ import deque_pop, my_deque', number=100000))
print(timeit.timeit('deque_popleft, my_deque', setup='from __main__ import deque_popleft, my_deque', number=100000))
