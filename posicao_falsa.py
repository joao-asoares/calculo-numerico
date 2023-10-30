from math import *

def false_position_method(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("A função f(a) e f(b) deve ter sinais opostos em [a, b].")
    
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        if abs(f(c)) < tol:
            return c
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    raise Exception("O método da posição falsa atingiu o número máximo de iterações.")

# Exemplo de uso:
def f(x):
    return x**3 - 4*x - 9

a = 1.0
b = 3.0
tolerance = 1e-6

root = false_position_method(f, a, b, tol=tolerance)
print("A raiz aproximada é:", root)
