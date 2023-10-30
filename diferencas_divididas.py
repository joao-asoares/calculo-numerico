def divided_differences(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("As listas de x e y devem ter o mesmo tamanho.")
    
    coefficients = [y[0]]
    for i in range(1, n):
        divided_diff = []
        for j in range(n - i):
            diff = (coefficients[j + 1] - coefficients[j]) / (x[j + i] - x[j])
            divided_diff.append(diff)
        coefficients.append(divided_diff[0])
    
    return coefficients

def interpolate(x, y, xi):
    coefficients = divided_differences(x, y)
    n = len(x)
    result = coefficients[0]
    factor = 1
    
    for i in range(1, n):
        factor *= xi - x[i - 1]
        result += coefficients[i] * factor
    
    return result

# Exemplo de uso:
x = [0, 1, 2, 3]
y = [1, 2, 3, 6]

xi = 1.5

interpolated_value = interpolate(x, y, xi)
print(f"O valor interpolado em xi = {xi} é aproximadamente: {interpolated_value}")
