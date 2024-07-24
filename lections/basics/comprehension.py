'================== comprehension ========================'
# генератор с помощью которго мы можем создать последовательность используя For

"""
результат For элемент in последовательность i for i in list1
результат for элемент в последовательность if фильтр i for i in list1 if i % 2 == 0
тело1 if условие else тело2 for элемент in в последовательность - условие
'четное' if i % 2 == 0 else 'нечетное' for i in range(1, 11)
"""


# comprehention = (i for i in range(1, 6)) 
# print(comprehention)

# генератор это итерируемый обьект который не хранит в себе полностью всю последовательность данных
# а создает их когда требуется 

# print(next(comprehention)) #1
# print(next(comprehention)) #2
# print(next(comprehention)) #3
# print(next(comprehention)) #4
# print(next(comprehention)) #5
# print(next(comprehention)) #StopIteration

# next - это функция которая запрашивает у генератора текущий элемент и генератор создает следующий элемент

'========================== синтаксический сахар ================================'
# list comprehension
# list_comprehension = list(i**2 for i in range(1, 6))
# # print(list_comprehension)
# list_comprehension2 = [1**2 for i in range(1, 6)] 

# list_comp = [i for i in range(1, 11)if i % 2 == 0]
# print(list_comp)

# list_comp2 = [i for i in range(1, 11, 2)]
# print(list_comp2)

# list3 = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list3.append(i)
# print(list3)

# list1 = []
# for i in range(5):
#     list1.append('hello')

# print(list1)    


# list_ = ['hello' for i in range(5)]
# print(list_)

# list_ = ['четное' if i % 2 == 0 else 'нечетное' for i in range(1, 11)]
# print(list_)


# list1 = [1, 'hello', 2, 'a', 2.3, 1000, 'world']
# list2 = [i for i in list1 if type(i) == str]
# print(list2)

# list2 = []
# for i in list1:
#     if type(i) == str:
#         list2.append(i)
# print(list2)


"============================ dict comprehension =================================="
# dict_ = dict( (i, i**2) for i in range(10))
# print(dict_)
# dict_ = {i: i**2 for i in range(10)}
# print(dict_) ##################################################

# dict1 = {"a":1, "b":2, "c":3}
# dict_ = {key: value for key, value in dict1.items()}
# print(dict1)
# print(dict_)


# dict1 = {"a":1, "b":2, "c":3}
# dict2 = {value: key for key, value in dict1.items()}
# print(dict2)

# dict1 = {
#     "a":[1,2,3,4],
#     "b":[10,15,16,17],
#     "c":[1,2,54]
# }
# dict2 = {key: sum(value) for key, value in dict1.items()}
# print(dict2)



# dict2 = {i:str(i) for i in range(1, 11)}
# print(dict2)


# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']

# dict1 = {}
# for ind in range(len(list1)):
#     key = list1[ind]
#     value = list2[ind]
#     dict1[key] = value
# print(dict1)

# dict_ = {list1[ind]: list2[ind] for ind in range(len(list1))}
# print(dict_)

# dict_ = dict(zip(list1, list2))
# print(dict_)


'========================= вложенные comprehension========================='

#1 
# dict1 ={}
# for i in range(1, 6):
#     key = i
#     value = [j for j in range(1, i + 1)]
#     dict1[key] = value
#     print(dict1)
#     dict1[key] = value

# #2
# dict_ = {i: [j for j in range(1, i + 1)]for i in range(1, 6)}
# print(dict_)

#3

# dict_ = {i: list(range(1, i + 1)) for i in range(1, 6)}
# print(dict_)

# list_ = []
# for i in range(10):
#     inner_list = []
#     for j in range(5):
#         inner_list.append('hello world')
#     list_.append(inner_list)
# print(list_)

#2
# list1 = [['hello world' for j in range(5)] for i in range(10)]
# print(list1)

#3
# list1 = [['hello world']*5 for i in range(10)]
# print(list1)

#4
# list1 = [['hello world']*5]*10
# print(list1)

list1 = [i for i in range(1, 6)]*10
print(list1)

list2 = [[j for j in range(1, 6)] for i in range(10)]
print(list2)