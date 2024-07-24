# ===числа===
# integers (int - целые числа )

age = 20
print(type(age)) # < class 'int'>
# type - возвращает тип данных к котрому относится переменная или значение 

# b = int('10j') # Valueerror: invalid literal for int() with base 10: '10j'
# print(type(b))
b = int ('10')
print(type(b))


# float - вещественные числа / десятичные 

price = 100.5
print (type(price)) #<class 'float'>


price2 = float(1) # 1.0
print(price2)

price3 = float('10.64')
print(price3) # 10.64
print(type(price3)) # <class 'float'>

# import decimal
from decimal import Decimal

a = Decimal('0.1')
print(a)
print (type(a))
print (a + a + a + a + a)

"===binary==="
a = bin(10)
print(a) # ob1010
print (int(a, 2)) #10


"===операции над числами==="

10 % 2 # нахождение остатка от от деления 
10 // 2 # целочисленное деление 
2 ** 3 # возведение в степень 
25 ** 0.5 # 5, нахождение квадратоного корня

# abs() - для получения модуля числа 

print(abs(-5))
print(abs(-285))

# round() - округление числа
print(round(1.3))
print(round(15.551))
print(round(1.3))
print(round(1.6))
print(round(13.49))
print(round(1.51))
print(round(1.51))


# """

# pyton3 <название файла> - запуск файла через терминал

# pyton3 - вход в pyton shell
# ctrl + d - выход из shell



# sqrt - функция нахождения квадратного корня числа. sqrt нужно импортировать 
# import math
from math import sqrt

# print(sqrt(25))
# print(sqrt(49))

"""
чтобы закоментировать выделенную область command + / отменить действие command + z
"""

#pow 
#1) возводит число в степень 
#2) находит остаток деления на 3 число

print(pow(2, 3)) # 2 ** 3 = 8
print(pow(2, 3 , 3)) # 2 ** 3 % 3 =2
print(2 ** 4)

#divmod() - функция 

print(divmod(8, 3)) # 2, 2
print(divmod(5, 2)) # 2, 1 
print(divmod(17, 5)) # 3, 2



print(type(price))

# import decimal
from decimal import Decimal

a = Decimal('0.4')
print(a)
print(type(a))
print(a + a + a + a + a)


print(2 + 7)


