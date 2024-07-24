"======строки========"
# строки это неизменяемый тип данных который предназначен для хранения текста заключенного в одинарные или в двойные кавычки 

str_ = 'строка с одинарными кавычками'
str2 = "строка с двойными кавычками"
srt3 = """
многострочный текст в двойных кавычках можно использовать 'любые' "кавычки"
"""
str = 'Don\'t'
str = "Don't"

"=====конкатенация======="

name = 'Nurs'
last_name = 'Osmon'
full_name = name + ' ' + last_name
print(full_name)

"=======экранизация строк========"

# '\n' - переносит на новую строку
#print('hello\nworld')
#print('hello')
#print('world')

# \t - табуляция
print('hello\tworld')

# '\'' - отображение '
# "\"" - отображение двойной кавычки

# \v - перенос на новую строку со смещением вправо на длину строки
print('hello\vworld\vmy\vname')

# \r - перенос каретки на начло строки
# print('hello\rhi')

"===форматирование строк==="

title = 'Iphone 15'
price = 1000
print(f'название: {title}\nЦена: {price}')

format2 = 'название: {}\nЦена: {}'
print(format2.format('iphone', '1000'))

"====методы строк===="
# методы это функции которые относятся к определенному классу (типу данных) к ним мы обращаемся через точку

#print(dir(str))  # - показывает все методы определенного типа данных

string = 'hello'
print(string.upper())

string1 = 'HELLO'
print(string1.lower())

print('Hello'.swapcase()) #переводит все символы в противоположный регистр

print('hello world'.title()) # переводит все первые буквы каждого слова в верхний регистр
print('hello world'.capitalize) # переводит только первую букву первого слова в верхний регистр


print('hello'.center(11, '-'))# центрует строку по указанному ограничителю (1 значение - ограничение, 2- значение это разделитель)

print('world'.count('w')) # возвращает количество вхождение заданного символа

print('hello'.startswith('h')) #проверяет начинается ли строка с заданного символа и возвращает тру или фолс
print('hello'. endswith('lo')) #проверяет заканчивается ли строка с заданного символа и возвращает тру или фолс



print('hello world'.islower())# проверяет находится ли строка полностью в нижнем регистре
print('hello worLd'.islower())

print('HELLO WORLD'.isupper())# проверяет находится ли строка полностью в нижнем регистре


# .isdigit() проверяет состоит ли строка полностью из чисел
print('17543678298376'.isdigit())

# .isalpha() проверяет состоит ли строка полностью из букв
print('hello'.isalpha())


print('hello123'.isalnum())
print('hello'.isalnum())
print('13476432'.isalnum())


print('hello world my name is Nur'.split())
# .split() - возвращает список который разделил по заданному разделителю на отдельные строки 
#['hello', 'world', 'my', 'name', 'is', 'Nur']

# .join() соединяет список по указанному разделителю
print('-'.join(['hello', 'world', 'my', 'name', 'is', 'Nur']))
#hello-world-my-name-is-Nur


# .strip()
string = '                                                                                                                  hello'
print(string.strip())

print(string.lstrip())
print(string.rstrip())




"======индексы====="
# индес это порядковый номер в последовательности (символа в строке) и начинается с нуля

'h e l l o w o r l d'
# 0 1 2 3 4 5 6 7 8 9 

string1 = 'hello world'
print(string1[0])
print(string1[5])
print(string1[-1])

# срез - подстрока строки

print(string1[0:5]) #hello
print(string1[0:4]) # hell
print(string1[6:11]) #world
print(string1[6:]) #world 
print(string1[6:-1]) #worl

print(string1[::-1]) # dlrow olleh
print(string1[::2]) #hlowrd

print(string1[1:5]) #ello
print(string1[1:5:2])


