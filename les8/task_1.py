"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""


from collections import deque, Counter


def haffman_tree(some_string):

    count = Counter(some_string)
    sorted_el = deque(sorted(count.items(), key=lambda item: item[1]))

    if len(sorted_el) != 1:
        while len(sorted_el) > 1:
            weight = sorted_el[0][1] + sorted_el[1][1]

            combination = {0: sorted_el.popleft()[0],
                           1: sorted_el.popleft()[0]}

            for idx, count_c in enumerate(sorted_el):
                if weight > count_c[1]:
                    continue
                else:
                    sorted_el.insert(idx, (combination, weight))
                    break
            else:
                sorted_el.append((combination, weight))
    else:
        weight = sorted_el[0][1]
        combination = {0: sorted_el.popleft()[0], 1: None}
        sorted_el.append((combination, weight))
    return sorted_el[0][0]


result = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        result[tree] = path

    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


my_string = "Hello, world!"
haffman_code(haffman_tree(my_string))
for idx in my_string:
    print(result[idx], end=' ')
