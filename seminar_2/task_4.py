"""Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число."""

print('Введите число N: ')
N = int(input())
import random
array = []
for i in range(0, N):
    array.append(random.randint(N*(-1), N))
print(f'Заданный список из N элементов: = {array}')

def read_file():
    with open('file.txt', 'r') as data:
        positions = list(map(int, data.readlines()))
        print(f'Индексы из файла = {positions}')
    return positions

f = read_file()
result = 1
for i in range(len(f)):
    result *= array[f[i]]
print(f'Произведение элементов = {result}')