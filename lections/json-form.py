'''============================ JSON =================================='''
# Javascript object notation - универсальный формат в котором можно хранить данные в типах данных понятных
# почти для всех языков програмирования

import json

json_list = "[1,2,3,4,5]"
print(type(json_list)) # <class 'str'>

python_list = json.loads(json_list)
print(type(python_list)) # <class 'list'>

# десереализация - перевод с json строки в pyton обьекты 
# .loads() - метод для десериализации с json строки 
# .load() - метод для десериализации с json файла

# сериализация - перевод pyton обьектов в json строку
# .dumps() - метод для сериалиализации в json строку
# .dump() - метод для сериалиализации в json файл


with open('test.json') as file:
    list_ = json.load(file)

print(list_)

with open('test.json', 'w') as file:
    list_ = json.dump(list_, file)
