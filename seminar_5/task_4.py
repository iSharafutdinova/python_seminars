"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах."""

def coding(text):
    count = 1
    result = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        result = result + str(count) + text[-1]
    return result

def decoding(text):
    number = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            result = result + text[i] * int(number)
            number = ''
    return result


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")