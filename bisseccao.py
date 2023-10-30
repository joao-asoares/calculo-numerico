"""
Discente: João Marcos de Assis Soares
Docente: Vitor Jose Petry
Trabalho sobre Método de Bissecção, Cálculo Númerico, semestre 2023/2
16/08/2023
"""

from math import *

# define a função f(x)
def f(x, a, b, c, d):
  return a*(x**3) + b*(x**2) + c*x + d

# define os extremos do intervalo
print("\nEsse programa determina a raiz de uma função polinomial (cúbica, quadrática, linear ou constante) em um intervalo [X, Y] determinado pelo usuário, utilizando o método de bissecção, com uma tolerância de f(raiz) < 10^-3\n")
print("Primeiro, insira os valores da função ax^3 + bx^2 + cx + d")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))

print(f"Função escolhida: {a}x^3 + {b}x^2 + {c}x + {d}\n")

inf = int(input("Digite o limite inferior do intervalo onde a raiz será procurada: "))
sup = int(input("Digite o limite superior do intervalo onde a raiz será procurada: "))

print(f"Intervalo escolhido: [{inf}, {sup}]")

# a tolerância indica o quão próximo a aproximação está da raiz
TOL = 0.001

if f(inf, a, b, c, d)*f(sup, a, b, c, d) < 0:           # verifica se há raiz nesse intervalo (se f(a) e f(b) forem positivo/negativo, f(a)*f(b) será negativo)
    med = (inf+sup)/2           # encontra o ponto médio do intervalo
    while abs(f(med, a, b, c, d)) > TOL:    # o loop para quando atinge a tolerância
        if f(inf, a, b, c, d)*f(med, a, b, c, d) < 0:   # Teorema de Bolzano
            sup = med           # atualiza os extremos do intervalo
            med = (inf+sup)/2
        else:
            inf = med
            med = (inf+sup)/2
    print(f"Raiz encontrada: {med}")                # a raiz foi encontrada
else:
    print("Não pode-se afirmar que há raiz nesse intervalo")