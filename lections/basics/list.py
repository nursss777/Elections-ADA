# '==========================list======================='


# # списки это изменяемый, индексируемый, упорядочный, интерируемый тип данных который предназначен для 
# # хранения любых данных в определенном порядке.



# list_ = [1, 2, 3, 'hello', [1, 2, 3], [[[1, 2]]], None, True, False]

# print(list_[1])
# print(list_[3][-1])
# print(list_[-1])
# print(list_[4][2])


# new_list = list('hello world')
# print(new_list)



# #range() - задает диапазон чисел, принимает 3 аргумента: 1 - начало диапазона, 2 - конец, 3 - шаг
# list2 = list(range(1, 11))
# print(list2)


# list3 = [1] * 10
# print(list3)


# '============================ методы списков ================================'
# # print(dir(list3))

# # .append() - добавляет элемент в конец списка


# list_ = []
# list_.append(1)
# print(list_)
# list_.append(1)
# list_.append(1)
# list_.append(1)
# print(list_)
# list_.append('hello')
# print(list_)


# # .pop() - удаляет элемнт из списка по индексу и результатом метода будет удаленный элемент (метод возвращает 
# # удаленный элемент), если не указать индекс - удалит с конца



# # popped_el = list_.pop(2)
# # print(popped_el)
# # print(list_)
# popped_el = list_.pop()
# print(popped_el, list_)
# popped_el = list_.pop()
# print(list_, popped_el)



# .remove() - удаляет элемент из списка по значению 
# list2 = [1, 2, 3, 4, True, 'hello']
# list2.remove(2)
# list2.remove(4)
# print(list2)      #[1, 3, True, 'hello']


# .count() - считает количество принятого элемента в списке
# print(list2.count(1))

# list3 = ['hello', 'hello', 'hello']
# print(list3.count('hello'))



# .index() - возвращают индекс первого вхождения принятого элемента 

# list3 = ['hello', 'hello', 'hello', 1, 4, 100, None]
# print(list3.index(1))


# .insert() - добавляет элемент в список по индексу

# list3 = ['hello', 'hello', 'hello', 1, 4, 100, None]
# list3.insert(0, 'world')
# print(list3)
# list3.insert(5, False)
# print(list3)


# .extend() - добавление элемента принятого списка в первый список, изменяя его 


list3 = ['hello', 'hello', 'hello', 1, 4, 100, None]
# list4 = [1, 2, 3, 4, {'a': 123}]
# list3.extend(list4)
# print(list3)



# .reverse() - изменяет список, расставляя его элементы в обратном порядке

# list3.reverse()
# print(list3)


#. sort() - сортирует список состоящий из элементов одного типа данных

# list3.sort()
# print(list3)
# TypeError: '<' not supported between instances of 'int' and 'str'



list5 = [1, 2, 3, 4, 100, 34, 894564773794657, 2000]
# list5.sort()
# print(list5)



# list5 = ['a', 'b', 'c', 'A', 'B', 'Hello']
# list5.sort()
# print(list5)

list5.sort(reverse=True)
print(list5)


# .clear() - очищает спиок
list5.clear
print(list5)


# len() - считает количество элементов в последовательности
list1 = [1, 2, 3, 4, 5, 66, 7, 8, [1, 2, 3]]
print(len(list1))



a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

name, age, city = ['Nur', 10, 'Bish']
print(name)
print(age)
print(city)