"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


import hashlib
from uuid import uuid4

salt = uuid4().hex
cache_obj = {}


def get_page(url):
    if cache_obj.get(url):
        print(f'Данный адрес {url} присутствует в кэше')
    else:
        result = hashlib.sha3_256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = result
        print(cache_obj)


get_page('http://geekbrains.ru/')
get_page('http://geekbrains.ru/')