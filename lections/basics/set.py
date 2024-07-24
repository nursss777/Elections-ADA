"=========================== Set ==========================="
# set это изменяемый неупорядочный итерируемый неиндексируемый тип данных который предназначен для хранения уникальных значений.
# множества могут хранить в себе только неизменяемый тип данных. Если использовать tuple то в них тоже должны быть неизменяемые типы данных

# set_ = {1, 2, 3, 4}
# set2 = {1, 1, 1, 1, 1, 2, 2, 3, 2, 3, 3, 3, 2, 11}
# print(set2) #{3, 1, 2, 11}

# set_ = {(1, 2, 3), 3, (4, 5, 6,), (1, 2, 3,)}
# print(set_) #{3, (4, 5, 6), (1, 2, 3)}

'======================== методы ==========================='
# print(dir(set_))

# # .add() - добавляет элементы в set
# set1 = {1, 2, 3, 4, 5}
# set1.add(6)
# set1.add(7)
# print(set1) #{1, 2, 3, 4, 5, 6, 7}

# .pop() - он удаляет случайный элемент из set (но есть принцип FIFO)

# set2 = {1, 2, 3, 4}
# popped = set2.pop()
# print(set2, popped)


# .remove() - удаляет элементы по значению

# set_ = {1, 2, 3}
# set_.remove(3)
# print(set_)


# .difference() (-)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1 - set2) #{1, 2}
# print(set2 - set1) #{4, 5}

# # .symetric_difference() - 
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.symmetric_difference(set2)) #{1, 2, 4, 5}

# .intersection() (&)
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# set2 = {4, 5, 6, 7, 8, 9, 10}
# print(set1.intersection(set2))
# print(set1 & set2) #{4, 5, 6, 7, 8}  {4, 5, 6, 7, 8}

# # .clear()
# set1 = {1, 2, 4, 5, 6}
# set1.clear()
# print(set1)

# .union() - возвращает множество которое содержит все элементы из всех переданных множеств

# set1 = {1, 2, 3}
# set2 = {True, False, (1, 2, 3)}
# set3 = {4, 5, 6, 7}

# result = set1.union(set2, set3)
# print(result) # {False, 1, 2, 3, 4, 5, 6, 7, (1, 2, 3)}

# .issubset() - проверяет является ли одно мнодество подмножеством другого (если все элементы одного множества присутствуют в другом
# то вернется Тrue)
# set1 = {1, 2}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2)) # True
# print(set2.issubset(set1)) # False

# # .issuperset()
# set1 = {1, 2}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issuperset(set2)) # False
# print(set2.issuperset(set1)) # True

# # .isdisjoint() - проверяет не имеют ли 2 множества общих элемент 

# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 7, 8, 9, 10}
# print(set1.isdisjoint(set2)) # True
# print(set2.isdisjoint(set1)) # False

# .discard() - удаляет элемент по указанному значению если элемент отсутствует то ошибка не вызывается

# set1 = {1, 2, 3, 4}
# set1.discard(3)
# print(set1)

# d1 = {"a": 100, "b": 200, "c":300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# print(d1["b"] == d2["b"])


# age = 25
# person = {"name": "Kelly", "age": 25, "city": "New york"}
# print(person['age'])


# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# result = set1.union(sample_list, sample_set)
# print(result)


# set1 = {6, 4, 2, 5, 7, 8, 10, 9}
# set1.remove(7)
# print(set1)



# set1 = {'Python', 'it', 'c++', 'java', 'programming'}
# set2 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set1 & set2)



# set2 = {'Python', 'it', 'c++', 'java', 'programming'}
# set3 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set3 - set2)


# set5 = {1, 2, 3, 5, 6}
# set5.add(4)
# popped = set5.pop()
# print(set5, popped)



menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
menu2 = {'besh': 130}
menu3 = {'drinks': 'coca, sprite, fanta'}
menu4 = {'lagman2': 135}
menu['plov'] = 111
menu.update(menu2)
menu.pop('borsh')
menu.update(menu3)
menu.update(menu4)
menu.pop('lagman')
print(menu)


# set1 = {'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
#          'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 
#          'symmetric_difference_update', 'union', 'update'}
# set2 = {'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'}
# print(set1 & set2)





# list_ = []
# list_.append(1)
# list_.append(2)
# list_.append(3)
# list_.append(4)
# list_.append(5)
# print(list_)