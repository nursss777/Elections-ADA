
while True:
    num1 = int(input('введите число: '))
    num2 = int(input('введите число: '))
    dot_ = input("Выберите операцию из следующих: +-*/%//: ")
    if dot_ == ('+'): 
        print(num1 + num2)
    elif dot_ == ('-'): 
        print(num1 - num2)
    elif dot_ == ('/'): 
        print(num1 / num2)
    elif dot_ == ('*'): 
        print(num1 * num2)
    elif dot_ == ('%'): 
        print(num1 % num2)
    elif dot_ == ('//'): 
        print(num1 // num2)
    else:
        print("Данной операции нет в системе!!!")
    ok = input('Хотите продолжить?: ')
    if ok == 'yes':
        pass
    elif ok == 'no':
        print('До свидания!!!')
        break

