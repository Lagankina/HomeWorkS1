
#

#a = int(input("Введите целое число: "))
#if (a < 10000 and a > 999):
#    print("Yes")
#else: print("no")

#Домашняя работа семинар 1

#Задача 2: Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0

#a = int(input("Введите трехзначное число: "))
#summa = 0
#while(a > 0):
    #x = a % 10
    #summa = summa + x
    #a = a//10
#print(summa)

#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#s = int(input("Общее количество журавливков: "))

#if(s % 6 == 0):
#    p = s // 6
#    c = s // 6
 #   print (f"Петя сделал журавликов {p} а Сережа {c}")
  #  k = (p + c) * 2
 #   print (f"Катя сделала журавликов: {k}")
#else: 
 #   n = s % 6
#print (f"Задача не может быть выполнена , oсталось лишних журавликов {n}")

#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#n = int(input("Введите номер билета: "))
#summa = 0
#sum = 0 

#a = n // 1000
#b = n % 1000

#while(a > 0):
 #   x = a % 10
#    summa = summa + x
#    a = a // 10

#while(b > 0):
 #   x = b % 10
#    sum = sum + x
#    b = b // 10

#if (summa == sum):
#    print("Счастливчик!!!")
#else:
#    print("Попробуйте еще раз!!")
#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

#Пример:*
#3 2 4 -> yes
#3 2 1 -> no

# a = int(input("Введите ширину шоколадки: "))
# b = int(input("Введите длину шоколадки: "))
# k = int(input("Сколь долек желаете?: "))

# resultA = k / a
# resultB = k / b

# if((resultA % 1 == 0 or resultB % 1 == 0) and (resultA < b or resultB < a)):
#     print(f"Можно отломить {k} дольки")
# else: 
#     print(f"Нельзя отломить {k} дольки")

#########################################################################################################
#ДОМАШНЯЯ РАБОТА СЕМИНАР 2

#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("Введите количество монет: "))

# array = [None for x in range(n)]

# for index in range(n):
#     array[index] = input("Введите монеты Орел или Решка: ")

# count = 0
# for value in array:
#     if (value.trim() == "Орел") :
#         count = count + 1
        
# min = 0
# if (count < n - count) :
#     min = count
# else :
#     min = n - count
    
# print(f"минимальное число монеток, которые нужно перевернуть: {min}")

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# S = int(input("Введите сумму чисел: "))
# P = int(input("Введите произведение чисел: "))

# for i in range(S):
#     for j in range(P):
#         if S == i + j and P == i * j:
#             print(i,j)
#             break
        
#############################################################################################################

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# N = int(input("Ввeдите число: "))
# num = 1

# while(num < N):
#     num *= 2
#     if(num > N):
#         num = num // 2
#         break
#     print(num)
#######################################################################################################

# 6.Даны положительные числа A, B, C. На прямоугольнике размера A x B размещено максимально возможное
# количество квадратов со стороной C (без наложений).
# Найти количество квадратов, размещенных на прямоугольнике. Операции умножения и деления не использовать.

# A = int(input("Введите сторну А: "))
# B = int(input("Введите сторону В: "))
# C = int(input("Введите стороны квадрата: "))
# count = 0
# for i in range(C, (A + 1), C):
#     for j in range (C,(B + 1), C):
#         count = count + 1
# print(count)
######################################################################################################
# 4*.Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км. Каждый следующий день он увеличивал 
# длину пробега на P процентов от пробега предыдущего дня (P — вещественное, 0 < P < 50).
# По данному P определить, после какого дня суммарный пробег лыжника за все дни превысит 200 км, 
# и вывести найденное количество дней K (целое) и суммарный пробег S (вещественное число).

# A = 10
# P = float(input("Введите процент ежедневного увеличения пробега: "))
# days = 1
# flag = True
# if 0 < P < 50:
#     for i in range(A, 201, P):
#         if A <= 201:
#             days += 1
#             print(days)
#     else: flag = False

# ////////////////////////////////////////////

# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 1 #9
# min_result = [len(list_1)]

# for element in list_1:
#     min_result.append(abs(k - element))

# min = 999999999999
# min_index = 0
# index = 0
# for index in range(1, len(min_result)):
#     if (min > min_result[index]):
#         min = min_result[index]
#         min_index = index

# print(list_1[min_index - 1])

# //////////////////////////////////////////////////////

# k = input("Введите слово: ").upper()
# summ = 0
# dict = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "S": 1, "T": 1, "R": 1, 
#             "D": 2, "G": 2,"B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, 
#             "V": 4, "W": 4, "Y": 4,"K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10,
#             "А": 1, "В": 1 , "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1, 
#             "Д": 2, "К": 2, "Л": 2, "М": 2, "П": 2, "У": 2, "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3, 
#             "Й": 4, "Ы": 4, "Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5, "Ш": 8, "Э": 8, "Ю": 8, "Ф": 10, "Щ": 10, "Ъ": 10}
# for i in k:
#     summ += dict[i]
# print(summ)
##########################################################################################################\
#     Семинар 4. Словари, множества и профилирование

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# import random

# n = int(input("Введите количество элементов первого множества: "))
# n_num = []
# for i in range(n):
#     n_num.append(random.randint(0,10))
# print(n_num)

# m = int(input("Введите количество элементов второго множества: "))
# m_num = []
# for i in range(m):
#     m_num.append(random.randint(0,10))
# print(m_num)

# n_num = set(n_num)
# m_num = set(m_num)

# res_num = n_num.intersection(m_num)
# print(f"Результирующий набор: {sorted(res_num)}")

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# import random

# N = int(input("Введите количество кустов: "))
# bush = []
# for i in range(N):
#     bush.append(random.randint(10,100))
# print(f"Cписок ягод:  {bush}")

# berry_max = 0
# for i in range(N - 1):
#     sum = bush[i - 1] + bush[i] + bush[i + 1]
#     if(sum > berry_max):
#         berry_max = sum
# print(berry_max)
            















