"""Задача №1. Вычислить число c заданной точностью d
Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$"""

from math import pi

d =  int(input("Сколько цифр после запятой числа π показать?\n"))
print(f'число π с заданной точностью {d} = {round(pi, d)}')