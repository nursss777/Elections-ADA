'================= функции =================='
# функция это именнованный блок кода который может возвращать результат и принимать аргументы

# def my_sum(x, y):
#     return x+ y

# res = my_sum(5, 6)
# print(res)


def my_len(obj):
    count = 0
    for element in obj:
        count += 1
    return count
res = my_len(['helo', 1, 2, 3, 4, True, False, [1, 2, 3]])     
print(res)