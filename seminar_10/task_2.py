"""Задача 2.
Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), 
если это число ранее встречалось в последовательности или NO, если не встречалось"""

a = [int(num) for num in input().split()]

for i in range(len(a)):
    x = a[i]
    y = a[:i]
    if x in y:
        print('YES')
    else:
        print('NO')