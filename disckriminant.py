from math import *

print('Введите x: ', end='')
x = float(input())
print('Введите y: ', end='')
y = float(input())
print('Введите z: ', end='')
z = float(input())

def func(D):
    if D < 0:
        print('Корней нет')
    elif D == 0:
        print('У уравнения единсвенный корень = ',round((-y)/(2*x)), 3)
    else:
        print('У уравнения два корня\nПервый корень = ', round(((-y)+sqrt(D))/(2*x), 3), '\nВторой корень = ', round(((-y)-sqrt(D))/(2*x)), 3)

func(y*y - 4*x*z)
    
