'================ циклы ====================='
# цикл это блок кода который отрабатывает несколько раз
# for - цикл который работает с итерируемым обьектом Цикл заканчивает работу когда он доходит до последнего элемента
# While -цикл который работает до тех пор пока условие верное

# list_ = ['hello world', 1, 2, 3, 30, None, True, False, [1, 2, 3,]]

# for element in list_:
#     print(element)

# for letter in 'hello world':
#     print(letter)


# n = 1
# while n <=10:
#     print(n)
#     n += 1

# 1 2 3 4 5 6 7 8 9 10

n = 0

# while n:
#     n += 1
#     print(0)
# не запустится 0 False


'================ оператор brake/ continue ==================='
# break - полностью прерывакт работу цикла (выйти из цикла)
# continue - пропускает итерацию и переходит к следующей 

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)
# 0 1 2 4 5 6 7 8 9 


# for i in range(10):
#     print(i)
#     if i == 3:
#         continue
# 1 2 3 4 5 6 7 8 9 


# for i in range (10):
#     print(i)
#     break 
# # 0 

# for i in range(10):
#     print(i)
#     if i == 3:
#         break


# for i in range (10):
#     if i == 3:
#         break 
#     print(i)


# for i in range(10):
#     if i < 3:
#         continue
#     print(i)
    # 3 4 5 6 7 8 9 

# list1 = [1, 1, 1, 1, 2, 3, 4, 5, 1, 59, 1, 1,]
# new_list = []

# for num in list1:
#     # if num == 1:
#     #     continue
#     # new_list.append(num)
#     if num != 1:
#         new_list.append(num)
# print(new_list)


# list1 = [1, 1, 1, 1, 2, 3, 4, 5, 1, 59, 1, 1,]

# while 1 in list1:
#     list1.remove(1)
# print(list1)


# for i in range(10):
#     for j in range(10):
#         print(i, j)


# for i in range (11):
#     print(i)

# n = 1
# while n <=10:
#     print(n)
#     n += 1


# for i in range (21):
#     if i % 2 == 0:
#         print(i)

# new_list = []

# for i in range(100):
#     if i % 3 == 0:
#         new_list.append(i)
#         print(i)


# new_list = []

# for i in range(100):
#     if i % 3 or i % 5 == 0:
#         new_list.append(i)
#         print(i)


# new_list = []

# for i in range(100):
#     if i % 3 or i % 9 or i % 2 == 0:
#         new_list.append(i)
#         print(i)


# for i in range (300):
#     if i == 237:
#         break
#     if i % 2 == 0:
#         print(i)
      



# my_string = "Бонет IPStorm, в который ранее входили лишь Windows-машины увеличился до 13500 зараженных систем"
# for i in my_string:
#     if i.isdigit():
#         print(int(i) * 2)