"""Дан текст: в первой строке записано число строк, далее идут сами строки. 
Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов 
или символами конца строки."""

count_of_strings = int(input())
lst = []
for i in range(count_of_strings):
    for element in input().split():
        lst.append(element)
        
print(len(set(lst)))