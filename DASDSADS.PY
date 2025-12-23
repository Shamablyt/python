

#2
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
        
#3
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
#4
#Вариант 1. Задание 1
number = int(input("Введите число: "))
if number < 0:
    number = -number
elif number == 0:
    number = 1

print(number)
#Задание 2. В1
text = input(("Введите текст:"))
if "." in text or "," in text:
    print(True)
else:
    print(False)
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
    print(True)
else:
    print(False)
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
#В3. Задание 1
num1 = int(input("Введите число: "))
if num1 > 0:
    num2 = num1 - 1
    num3 = num1 + 1
    print(num1, num2, num3)
elif num1 < 0 or  num1 == 0:
    num1 = 1
    num2 = num1 - 1
    num3 = num1 + 1
    print(num1, num2, num3)
#В3. Задание 2
filename = input(("Введите имя файла с расширением: "))
if ".doc" in filename:
    print("Word file")
elif ".py" in filename:
    print("Python file")
elif ".txt" in filename:
    print("Text file")
#В3. Задание 3
d = float(input("Введите первую сторону: "))
f = float(input("Введите вторую сторону: "))
s = float(input("Введите третью сторону: "))

if d == f == s:
    print("Равносторонний треугольник")
elif d == f or f == s or s == d:
    print("Равнобедренный треугольник")
else:
    print("Разносторонний треугольник")
#В4. Задание 1
textv4 = "important information in one line"
letter = input("Введите букву: ")
if letter in textv4:
    print(True)
else:
    print(False)
#В4. Задание 2
side1 = float(input("Введите первую сторону: "))
side2 = float(input("Введите вторую сторону: "))
if side1 <= 0 or side2 <= 0:
    print("Стороны должны быть положительными")
else:
    if side1 == side2:
        print("Фигура: Квадрат")
    else:
        print("Фигура: прямоугольник")
    area = side1 * side2
    print(f"Площадь: {area}")
#В4. Задание 3
question = input("Как твои дела?")
if ["хорошо", "нормально", "отлично"] in question:
    print("😊")
elif ["плохо", "не хорошо", "..."]:
    print("😔")
else:
    print("😐")
#В5. Задание 1
numv5 = int(input("Введите первое число: "))
numv52 = int(input("Введите второе число: "))

if numv5 > numv52:
    numv5 = numv5 ** numv52
elif numv5 < numv52:
    numv52 = numv52 ** numv5
elif numv5 == numv52:
    sum = numv5 + numv52
    print(sum)
#В5. Задание 2
new_message = "Hello! How are you?"
user_message = input(("Введите ваш ответ: "))

if new_message[0] == user_message[0]:
    print(True)
else:
    print(False)
#В5. Задание 3
a1 = float(input("Введите длину первого отрезка: "))
b1 = float(input("Введите длину второго отрезка: "))
if a1 == b1:
    print("Отрезки равны")
elif a1 > b1:
    diff = a1- b1
    print(f"Первый отрезок длинее на {diff}")
else:
    diff = b1 - a1
    print(f"Второй отрезок длинее на {diff}")

       #В6. Задание 1
string = input("Введите строку: ")

if len(string) > 0:
    print(string[0] == string[-1])
else:
    print("Строка пустая")
#В6. Задание 2
numb = int(input("Введите число: "))

if numb % 2 == 0:
    result = numb ** 2
    print(f"Число кратно 2. {numb}^2 = {result}")
elif numb % 3 == 0:
    result = numb ** 3
    print(f"Число кратно 3. {numb}^3 = {result}")
else:
    result = numb * 100
    print(f"Число не кратно 2 и 3. {numb} * 100 = {result}")
#В6. Задание 3
numv6 = float(input("Введите первое число: "))
numv61 = float(input("Введите второе число: "))

if numv6 < 0 and numv61 < 0:
    print(False)
elif numv6 >= 0 and numv61 >= 0:
    print(True)
else:
    if numv6 < 0:
        numv6 += 1000
    if numv61 < 0:
        numv61 += 1000
    print(f"Первое число: {numv6}, второе число: {numv61}")
#В7. Задание 1
string = input("Введите строку: ")

if len(string) > 0:
    last_char = string[-1]
    print(last_char in ["я", "и", "е", "ю"])
else:
    print("строка пустая")
#В7. Задание 2
a2 = int(input("Введите первую сторону треугольника: "))
b2 = int(input("Введите вторую сторону треугольника: "))
c2 = int(input("Введите трктью сторону треугольника: "))

if a2 > 0 and b2 > 0 and c2 > 0 and (a2 + b2 > c2) and (a2 + c2 > b2) and (b2 + c2 > a2):
    print(True)
else:
    print(False)
#В7. Задание 3
nuum = int(input("Введите число: "))
last_digit = abs(nuum) % 10

if last_digit == 0:
    result = nuum ** 10
    print(f"Последняя цифра 0. Число в степени 10: {result}")
elif last_digit == 1:
    remainder = nuum % 3
    print(f"Последняя цифра 1. Остаток от деления на 3: {remainder}")
elif last_digit == 2:
    result = nuum // 2
    print(f"Последняя цифра 2. Целочисленное деление на 2: {result}")
else:
    result = nuum ** 2
    print(f"Последняя цифра {last_digit}. Число в квадрате: {result}")
#В8. Задание 1
password = input("Введите пароль: ")

if len(password) < 8 or "23" in password:
    print(False)
else:
    print(True)
#В8. Задание 2
pc_number = 777

nuum1 = int(input("Введите первое число: "))
nuum2 = int(input("Введите второе число: "))

if (nuum1 < pc_number < nuum2) or (nuum2 < pc_number < nuum1):
    print(True)
else:
    print(False)

#В8. Задание 3
lamp_1 = 0
lamp_2 = 0

choice = input("Какую лампочку зажечь? (введите 1 или 2): ").strip()

if choice == "1":
    lamp_1 = 1
    print(f"Лампочка 1 зажжена. lamp_1 = {lamp_1}, lamp_2 = {lamp_2}")
elif choice == "2":
    lamp_2 = 1
    print(f"Лампочка 2 зажжена. lamp_1 = {lamp_1}, lamp_2 = {lamp_2}")
else:
    print("Обе лампочки не горят")
#В9. Задание 1
switch_1 = False
switch_2 = False

answer = input("Включить? ")

if answer == "да":
    switch_1 = True
    switch_2 = True
    print("Всё включено")
    print(f"switch_1 = {switch_1}, switch_2 = {switch_2}")
else:
    print(f"switch_1 = {switch_1}, switch_2 = {switch_2}")

#В9. Задание 2
numm = int(input("Введите число: "))

if numm > 0:
    if numm % 2 == 0:
        print(True, "even")
    else:
        print(True, "odd")
else:
    print(False)

#В9. Задание 3
string = input("Введите строку: ")

if string.startswith("/"):
    print("command")
else:
    print("It’s string")
#В10. Задание 1
string = input("Введите строку: ")

if len(string) == 0:
    print(None)
elif len(string) <= 5:
    print("short")
elif 6 <= len(string) <= 10:
    print("normal")
else:  
    print("long")

#В10. Задание 2
numv10 = int(input("Введите целое число: ")) 

if numv10 < 0:
    numv10 = 1_000_000
    print(numv10)
elif numv10 == 0: 
    numv10 = 2
    result = numv10 ** 2
    print(result)
else:
    result = numv10 ** 3 
    print(result)

#В10. Задание 3
number_1 = 10
number_2 = 100

user_num = int(input("Введите ваше число: "))

if number_1 <= user_num <= number_2:
    print(True)
else:
    print(False) 
    
#1
m = ["Круг", 0.25, "Квадрат", "треугольник", 15, "круг", "овал", 10]
m.remove(0.25)
m.remove(15)
m.remove(10)
print(m)
#2
abc =  ["A", "B", "C", "D", "E", "F", "G"]
del abc[1:5]
print(abc)
#3
numbers = [1,4]
numbers.insert(1,2)
numbers.insert(2,3)
print(numbers)
#4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass = [x for x in mass if x >= 0]
sorted_asc = sorted(mass)
sorted_desc = sorted(mass, reverse = True)
print(sorted_asc)
print(sorted_desc)
#5
n = int(input("Введите количество чисел: "))

negative_numbers = []
positive_numbers = []
zeros = []             

for i in range(n):
    num = float(input("Введите число: "))
    
    if num < 0:
        negative_numbers.append(num)
    elif num > 0:
        positive_numbers.append(num)
    else: 
        zeros.append(num)

if negative_numbers:
    sum_negative = sum(negative_numbers)
    print(f"Сумма отрицательных чисел: {sum_negative}")
else:
    print("Отрицательных чисел нет")

if positive_numbers:
    avg_positive = sum(positive_numbers) / len(positive_numbers)
    print(f"Среднее арифметическое положительных чисел: {avg_positive}")
else:
    print("Положительных чисел нет")

if zeros:
    stars_list = ['*' for _ in range(len(zeros))]
    
    print(f"Количество звёзд: {len(zeros)} {stars_list}")
else:
    print("Нулей нет")
    
print("\nРаспределение чисел:")
print(f"Отрицательные: {negative_numbers}")
print(f"Положительные: {positive_numbers}")
print(f"Нули: {zeros}")

#1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("matrix:")
for row in matrix:
    print(row)

print("\nнечётные числа matrix")
odd_numbers = []
even_count = 0

for row in matrix:
    for num in row:
        if num % 2 != 0:
            odd_numbers.append(num)
            print(num, end=" ")
        else:
            even_count += 1

print(f"\n\nкол-во чётных: {even_count}")
#2
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]

answer_matrix = [[0 for _ in range(len(matrix_1[0]))] for _ in range(len(matrix_1))]

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]

print(answer_matrix)

for i, row in enumerate(answer_matrix):
    row_sum = sum(row)
    print(f"{row} сумма строки: {row_sum}")
#3
fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], 
          ['lime', 'lemon'], ['Mango', 'grapes']]

for row in fruits:
    for fruit in row:
        if fruit[0].isupper():
            print(fruit) 
                     




