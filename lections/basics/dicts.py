# '========= словари ========='
# # dict - изменяемый итерируемый неупорядоченный неиндексируемый тип данных для хранения данных в паре {ключ: значение}

# # user = {
# #     "name": 'Nur', 
# #     "city": 'Bishkek',
# #     "country": 'KG',
# # }

# # print(user['name'])
# # print(user['city'])

# # # ключами в словаре могут быть только неизменяемый тип данных


# # dict_ = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
# # print(dict['a']) # 4 если ключи одинаковые то сохранится только последнее значение


# # dict1 = {'a': 1, 'b': 2}
# # print(dict1)

# dict3 = dict( ["ab", "cd", "ef"])
# print(dict3)


# dict4 = {}
# dict4['name'] = 'Nur'
# print(dict4)

# '=============== методы словарей =================='
# # print(dir(dict4))
# # get - метод который возвращает значение по ключу если же ключа нет то возвращает None или дефолтное значение

# user = {
#     "name": 'Nur', 
#     "city": 'Bishkek',
#     "country": 'KG',
# }
# print(user.get('id'))
# print(user.get('name'))
# print(user.get('city'))


# # .pop() - метод который удаляет пару по ключу и возвращает значение
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# popped = dict_.pop('a')
# print(dict_)
# print(popped)
# # {'b': 2, 'c': 3}
# # 1


# # popitem() - метод который удаляет последнюю пару и возвращает ее
# # dict5 = {'a': 1, 'b': 2, 'c': 3}
# # popped = dict5.popitem()
# # print(dict5)
# # print(popped)
# # {'a': 1, 'b': 2}
# # ('c', 3)


# # # .update() - расширяет словарь парами из второго словаря

# # dict1 = {1: 'a', 2:'b', 3:'c'}
# # dict2 = {2:'c', 4:'d'}
# # dict1.update(dict2)
# # print(dict1)
# # # {1: 'a', 2: 'c', 3: 'c', 4: 'd'}

# # # .clear() - удаляет все пары в словаре
# # dict1.clear()
# # print(dict1)


# # .fromkeys() - метод для создания словаря используя список ключей 

# dict1 = dict.fromkeys('hi')
# print(dict1)  # {'h': None, 'i': None}


# dict2 = dict.fromkeys([1, 2, 3, 4])
# print(dict2)   # {1: None, 2: None, 3: None, 4: None}

# dict3 = dict.fromkeys([1, 2, 3], 'hello')
# print(dict3)   # {1: 'hello', 2: 'hello', 3: 'hello'}


# '============+++=================================++========++===+===+==+============================================++++=========='
# # keys, values, items
# # keys - метод который возвращает ключи 
# # values - метод который возвращает значения 
# # items - метод который возвращает пары ключ - значение в виде tuple

# # user = {
# #     'name': 'Nur',
# #     'city': 'Bish',
# # }

# # print(user.keys())
# # print(user.values())
# # print(user.items())






# user = {
#     "name": 'Nur', 
#     "city": 'Bishkek',
#     "country": 'KG',
# }

# for key in user:
#     print(key)
# # при итерации приходят ключи 

# for key in user.keys():
#     print(key)


# for value in user.values():
#     print(value)
# # при итерации dict_values приходят значения

# for items in user.items():
#     print(items)     
# # ('name', 'Nur')
# # ('city', 'Bishkek')
# # ('country', 'KG')
    


# for key, value in user.items():
#     print(key, value)



# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {}
# for key, value in dict1.items():
#     dict2[value] = key

# print(dict2)
