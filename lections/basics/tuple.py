'=========== tuple ==========='
# кортеж(tuple) - неизменяемый, упорядочный, интерируемый тип данных, предназначенный для хранения любых данных в определенном 
# порядке (в целом не отличается от списков, просто он неизменяемый поэтому занимает меньше памяти)

# tuple1 = (1, 2, 3)
# print(type(tuple)) # <class 'tupple'>
# tuple2 = (5)
# print(type(tuple)) # <class int>

# tuple2 = tuple('hello')
# print(tuple2)

# tuple4 = (1, 2, 3, [1, 2, 3,])
# tuple4[-1].append('hello')
# print(tuple4)



# tuple6 = tuple([1, 2, 3, 1, 2, 3, 'hello'])
# print(tuple6)

# '========== методы ========='
# # .count() - считает количество принятого элемента в кортеже (tuple)

# tuple_ = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, False, True)
# print(tuple_.count(1))

# tuple7 = ('hello', 'hello', 'hello')
# print(tuple7.count('hello'))


# # .index() - возвращает индекс первого вхождения принятого элемента

# tuple8 = (1, 2, 1, 1, 1, 1, 1, 'hello', 100)
# print(tuple8.index(100))



# tuple1 = [(2, 3, 4, 5, 6), ("hello",), (1,), (4,), ('world',)]
# print(tuple1)



# tuple2 = ['hello', 'hello', 'hello', 1, 4, 100, None]
# print(tuple2.index(100))



# list_ = [67, 'hello', 6, 36, True, False]
# print(list_)



list2 = ['hello', 'world', 'my_name', 'is', 'Nur']
list2.join('hello', 'world')
print(list2)




