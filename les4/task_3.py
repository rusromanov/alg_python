"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


user_number = int(input('Введите целое число: '))

print(timeit.timeit(f'revers({user_number})', setup='from __main__ import revers', number=1000))
print(timeit.timeit(f'revers_2({user_number})', setup='from __main__ import revers_2', number=1000))
print(timeit.timeit(f'revers_3({user_number})', setup='from __main__ import revers_3', number=1000))

cProfile.run('revers(9999999999)')
cProfile.run('revers_2(9999999999)')
cProfile.run('revers_3(9999999999)')
