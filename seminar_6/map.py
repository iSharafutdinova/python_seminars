A= list(map(int, input('Введите координаты точки A (X, Y) через пробел (например: 3 6):').split()))
B= list(map(int, input('Введите координаты точки B (X, Y) через пробел (например: 2 1):').split()))
result = (((B[0] - A[0])**2) + ((B[1] - A[1])**2))**(1/2)
print(f'Расстояние между двумя точками пространства = {round(result, 2)}')