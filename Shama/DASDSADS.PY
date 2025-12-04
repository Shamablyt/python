

№2
#1
bytes_input = int(input("Введите количество байт: "))
bits_output = bytes_input * 8
print(f"{bytes_input} байт (a) = {bits_output} бит (a)")
#2
print('Электронная книга по программированию на английском языке состоит из S страниц.\n'
    'В среднем на странице С строк по N символов.\n'
    'Используется кодировка UTF-8. Определите объём текстового файла в Кбайтах.')
s = int(input('Введите кол-во страниц: '))
c = int(input(' Введите кол-во строк на странице:'))
n = int(input('Введите кол-во символов на странице: '))
print(f'Электронная книга по программированию на английском языке состоит из {s} страниц.'
f'\nВ среднем на странице {c} строк по {n} символов.'
'\пИспользуется кодировка UTF-8. Определите объём текстового файла в Кбайтах.')
r1 = s * c * n
r2 = r1 / 1024
print(f'{s} * {c} * {n} = {r1} - Всего символов в книге.')
print(f'{r1} / 1024 = {r2} - Кбайт.')
print(f'Ответ: {r2}.')
        
№3
    #1
minutes = int(input("Введите минуты:"))
hours = minutes // 60
remaininng_minutes = minutes % 60

print(f"{hours}")
print(f"{remaininng_minutes}")

#2
a = int(input())
b = int(input())
h = int(input())

if h < a:
    print("Недосып")
elif h > b:
    print("Пересып")
else:
    print("Это нормально")

#3
d = float(input())
f = float(input())
g = float(input())

p = (d + f + g) / 2
s = (p * (p-d) * (p-f) * (p-g)) ** 0.5
print(s)

#4
figure = input()

if figure == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    s = (p * (p-a) * (p-b) * (p-c)) ** 0.5
elif figure == "прямоугольник":
    a = float(input())
    b = float(input())
    s = a * b
elif figure == "круг":
    r = float(input())
    s = 3.14 * r ** 2
print(s)
#5
n = int(input())
last_digit = n % 10
last_two_digits = n % 100

if 11 <= last_two_digits <= 14:
    ending = "программистов"
elif last_digit == 1:
    ending = "программист"
elif 2 <= last_digit <= 4:
    ending = "программиста"
else:
    ending = "программистов"

print(n, ending)
#6
ticket = input()

if len(ticket) != 6:
    print("Неверный ввод")
else:
    sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    if sum1 == sum2:
        print("Счастливый")
    else:
        print("Обычный")
№4
#Вариант 1. Задание 1
number = int(input("Введите число: "))
if number <0:
    number = -number
elif number == 0:
    number = 1

print(number)
#Задание 2. В1
text = input(("Введите текст:"))
if "." in text or "," in text:
    print("True")
else:
    print("False")
#Задание 3. В1
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
if a % 3 == 0 and b % 3 == 0:
    print("True")
elif a % 3 == 0 or b % 3 == 0:
    print("Одно число делится на 3")
else:
    print("False")
#В2. Задание 1
n = int(input("Введите число: "))
if n > 100:
    print("*")
elif n < 0:
    pass
else:
    print("*" * n)
#В2. Задание 2
text1 = input(("Введите первый текст: "))
text2 = input(("Введите второй текст: "))
if text1 == text2:
    print("True")
else:
    print("False")
#В2. Задание 3
r = int(input("Введите r (0-255): "))
g = int(input("Введите g (0-255): "))
b = int(input("Введите b (0-255): "))

if r == 0 and g == 0 and b == 0:
    print("Черный цвет")
elif r == 255 and g == 255 and b == 255:
    print("Белый цвет")
elif r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b == 0:
    print("Зелёный цвет")
elif r == 0 and g == 0 and b == 255:
    print("Синий цвет")
else:
    print("Нет цвета")
    


    





