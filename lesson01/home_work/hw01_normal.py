
__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

a = int(input("Введите ваш возвраст: "))
i = 0
while a != 0:
    b = (a % 10)
    a = a // 10
    if i <  b:
       i = b
print(i)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input("Введите первое чилсо: "))
b = int(input("Введите второе чилсо: "))

a = a + b
b = a - b

a = a - b

print(a)
print(b)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
a = int(input())
b = int(input())
c = int(input())

if ( b*b - 4*a*c ) > 0:
   d = math.sqrt( b*b - 4*a*c )
   x1 = (-b + d)/ (2*a)
   x2 = (-b - d) / (2*a)
   print(x1)
   print(x2)
elif ( b*b - 4*a*c ) == 0:
    d = 0
    x1 = -b/ (2*a)

    print(x1)
else:
    print("Дискриминатн отрицательным быть не может")

