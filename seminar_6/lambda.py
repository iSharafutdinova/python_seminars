N = int(input('Введите число N для поиска набора произведений чисел от 1 до N: '))
data = list(range(1, N+1))
print(f'Исходный список от 1 до N: {data}')

result = list(map(lambda x: x * x, data))
print(f'Cписок их квардатов чисел от 1 до N: {result}')