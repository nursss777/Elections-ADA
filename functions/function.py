'================================================Функции=================================='
# Функция это именованный блок кода который может принимать аргументы и возвращать результат
# def my_sum(x,y):
#     return x + y
# res = my_sum(5,6)
# print(res)
# def my_len(obj):
#     count = 0
#     for element in obj:
#         count += 1
#     return count
# res = my_len(['hello',1,2,3,4,True,False[1,2,3]])
# print(res)
"""
DRY - (dont repeat yourself), функции соблюдают этот принцип 
"""

# ПАРАМЕТРЫ это переменные внутри функции значения которых мы задаем при определении функции 
# АРГУМЕНТЫ это переменные которык мы передаем при вызове функции

# def my_sum(x,y): # OBJ - параметр
#     return x + y
# res = my_sum(5,6)
# print(res)
# def my_len(obj):
#     count = 0
#     for element in obj:
#         count += 1
#     return count
# res = my_len(['hello',1,2,3,4,True,False[1,2,3]]) - #аргумент


'=============== виды параметров =============='

# 1) обязательные 
# 2) не обязательные
# 2.1 с дефолтным значнием
# 2.2) args (все позиционные аргументы которые не попади в обязательные и с дефолтным значением)
# 2.3) лцфкпы (все лишние именнованные аргументы)

"===== виды аргументов ======"

# 1) позиционные (по позиции)
# 2) именнованные (по названию(параметр = значение))

# def add_or_add_10(num1:int num2 = 10):
#     return num1 + num2


# print(add_or_add_10(5))

"========================= * ========================="

# list1 = list(range(1, 11))
# list2 = [* range(1, 11)]
# print(list1)
# print(list2)


# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {**dict1}
# list1 = [*dict1]
# print(dict1)
# print(dict2)
# print(list1)


# def fun(a, b=10, *args, **kwargs):
#     print('a-', a)
#     print('b-', b)
#     print('*args -', args)
#     print('*kwargs -', kwargs)

# fun(3)  
# a- 3
# b- 10
# *args - ()
# *kwargs - {}



# "============== lambda =================="
# # lambda -анонимная функция которая записывается в одну строку
# lambda1 = lambda x: x**10
# print(lambda1(10))

# '=======калькулятор======'

# calc = {
#     '+': lambda n1, n2: n1 + n2,
#     '-': lambda n1, n2: n1 - n2,
#     '*': lambda n1, n2: n1 * n2,
#     '**': lambda n1, n2: n1 ** n2,
#     '/': lambda n1, n2: n1 / n2,
#     '//': lambda n1, n2: n1 // n2,
#     '%': lambda n1, n2: n1 % n2,
# }

# def main():
#     try:
#         num1 = int(input('введите число 1: '))
#         num2 = int(input('введите число 2: '))
#         oper = input('введите оператор: ')
#         func = calc[oper]
#         res = func(num1, num2)

#         print(num1, oper, num2, '=', res)
#     except ValueError:
#         print('введите число!')
#     except KeyError:
#         print("такой операции нет!")
#     except ZeroDivisionError:
#         print("на ноль делить нельзя")

# while True:
#     main()
#     if input('завершить (yes/no)?'). lower() == 'yes':
#         break


# db = [
#     {'name': 'Nur', 'password':hash('Nur123') }, 
#     {'name': 'Nur2', 'password': hash('12345678') }
# ]

# def in_database(name):
#     for user in db:
#         if user['name'] == name:
#             return True
#     return False

# def register(name, password1, password2):
#     if in_database(name):
#         raise Exception("пользователь с таким именем уже существует!")
#     if password1 != password2:
#         raise Exception('пароли не совпадают!')
#     user = {'name': name, 'password':hash(password1)}
#     db.append(user)
#     return 'вы успешно зарегистрировались!'

# def login(name, password):
#     if not in_database(name):
#         raise Exception('пользователь не найден!')
#     for user in db:
#         if user['name'] == name:
#             if user['password'] != hash(password):
#                 raise Exception('пароль не верный!')
#     return 'вы успешно вошли в систему!'      

# def main():
#     print('добро пожаловать!')
#     while True:
#         try:
#             action = input('Register:1, Login:2, Quit:3\n')

#             if action == '3':
#                 break
#             elif action == '1':
#                 name = input('введите имя: ')
#                 p1 = input('введите пароль: ')
#                 p2 = input('повтоите пароль: ')
#                 print(register(name, p1, p2))
#             elif action == '2':
#                 name = input('введите имя: ')
#                 password = input('введите пароль: ')
#                 print(login(name, password))
#             else:
#                 print('не корректный выбор')
#         except Exception as error:
#             print(error)

# main()
                













# print(db[-1]['password'])



