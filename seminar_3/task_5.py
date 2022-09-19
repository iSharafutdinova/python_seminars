"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]"""

def fibonacci(num):
    if num in [1, 2]:                       
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def nega_fibonacci(num):
    if num == 1:                       
        return 1
    elif num == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, num):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
number = int(input('Введите число: '))
for n in range(1, number + 1):
    list.append(fibonacci(n))
    list.insert(0, nega_fibonacci(n))
print(list)