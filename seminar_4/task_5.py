"""Задача №5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов."""

import random

def write_in_file(name,st): # запись в файл
    with open(name, 'w') as data:
        data.write(st)

def create_num(): # создание случайного числа от 0 до 100
    return random.randint(0,101)

def create_mn(k): # создание коэффициентов многочлена
    lst = [create_num() for i in range(k+1)]
    return lst
    
def create_str(sp): # создание многочлена в виде строки
    lst= sp[::-1]
    line = ''
    if len(lst) < 1:
        line = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                line += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    line += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                line += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    line += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                line += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                line += ' = 0'
    return line

def sq_mn(k): # получение степени многочлена
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def k_mn(k): # получение коэффицента члена многочлена
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def calc_mn(st): # разбор многочлена и получение его коэффициентов
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    list = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        list.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            list.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            list.append(0)
            i += 1
        
    return list
    
# создание двух файлов
k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_in_file("file_1.txt", create_str(koef1))
write_in_file("file_2.txt", create_str(koef2))

# нахождение суммы многочлена
with open('file_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_in_file("file_res.txt", create_str(lst_new))
with open('file_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")