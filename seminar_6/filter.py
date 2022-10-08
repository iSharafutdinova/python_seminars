data = list(map(int, input("Введите числа через пробел:\n").split()))
print(f'Исходный список: {data}')

def found_odds(i):
    if(i % 2) == 0:
        return True
    else:
        return False

result = filter(found_odds, data)

print("Отфильтрованный список (четные числа исходного списка): ", list(result))