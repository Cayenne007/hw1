


#Задача 1
# def plus(*text):
#     result = 0
#     for num in text:
#         result += int(num)
#     return result

# text = input('Введите трехзначное число : ')
# print('Результат: ', plus(text[0], text[1], text[2]))

#Задача 2
# s = int(input('Введите общее количество журавликов: '))
# if s%6 != 0:
#     print('Указано некорректное число')
# else:  
#     x = int(s/6) 
#     print('Петя и Сережа сделали по: ',x,', а Катя сделала: ',s-2*x)

#Задача 3
# def isLucky(number):
#     if len(number) != 6:
#         return False
    
#     return plus(number[0],number[1],number[2]) == plus(number[-1],number[-2],number[-3])

# number = input('Введите номер вашего билета: ')
# if isLucky(number):
#     print('Ура! Ваш билет счастливый!')
# else:
#     print('У вас обычный билет. Повезет в следующий раз')


#Задача 4
lenght = int(input('Укажите длину: '))
width = int(input('Укажите ширину: '))
k = int(input('Укажите какое количество долек хотите отрезать: '))


if k <= (lenght*width) and (k == width or k%width == 0):
    print('yes')
else:
    print('no')
