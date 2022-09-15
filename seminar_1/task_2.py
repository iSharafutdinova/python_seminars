"""Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат"""

def predicate(X, Y, Z):
    print(f"¬({X} ⋁ {Y} ⋁ {Z}) = ¬{X} ⋀ ¬{Y} ⋀ ¬{Z} is {(not (X or Y or Z)) == (not X and not Y and not Z)}")
    return (not (X or Y or Z)) == (not X and not Y and not Z)

if (predicate(0, 0, 0) and predicate(0, 0, 1) and predicate(0, 1, 0) and predicate(0, 1, 1) 
and predicate(1, 0, 0) and predicate(1, 0, 1) and predicate(1, 1, 0) and predicate(1, 1, 1)):
    print('true')
else:
    print('false')