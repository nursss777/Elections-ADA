"================================= области видимости ========================="
# LEGB - logal enclosed global built-in

'================================ Built in ==================================='
# Встроенное пространство имен (list, sum, dict, print, input)

'================================= Global ======================================'
# все переменные которые мы создали внутри одного файла
# чтобы посмотреть все глобаьные переменные, можно использовать globals()

# a = 5
# b = 'hello'
# print(globals())

'======================= local ======================'
# локальные пространство имен - переменные созданные внутри функции(цикла и условия)

# a = 10

# def func(a, b):
#     print('GLOBALS', globals())
#     print('LOCALS', locals())
#     print(a, b)
# func(5, 7)


"========================== enclosed ================================"
# замкнутое пространство имен это локальное пространство у которго есть внутреннее локальное пространство
var = 'global'
def func():
    # локальное простанство для глобального пространства
    # замкнутое пространство потому что есть более локальное пространство
    var = 'enclosed'
    def inner_func():
        # локальное пространство для пространства func
        var = 'local'
        print(var)
    print(var)
    inner_func()

print(var) 
func()
    
count = 1 

def increase_count():
    global count
    print(count)
    count += 1



increase_count()
increase_count()
increase_count()
increase_count()
increase_count() 