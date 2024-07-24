"============Логические операторы============="
# логические операторы - выражения возвращают ТРУ, если верно, если нет-Фолс

"===Равенство==="
5 == 5 # сравнения True
# name = 5 - оператор присваивания 
2 == 5 # false 

"===НЕ==="
4!= 5 # True
5!= 5 # False

"===Больше==="
4 > 4 # False
10 > 5 # True

"===Больше или равно==="
10 >= 4 # True
1 > 10 # False
10 <= 20 # True 
10 <= 10 # True
20 <= 10 # False 

print('5' ==5)
print('Hello' == 'hello')


"=== and, or, not ==="
#and - и 
#or - или
#not - не 
 

a = 5 
b = 3

print(a == b and a > b ) # False
print(a == b or a > b ) # True

print(not True)
print(not False)

print (not a == 5) # False

print(bool(1))
print(bool(0))

print(bool('hello'))
print(bool(' '))
print(bool(''))
"=== is ==="
a = 5
b = 5 
print(a == b)
print(a is b)


#None 
print(bool(None))
print(bool('None'))