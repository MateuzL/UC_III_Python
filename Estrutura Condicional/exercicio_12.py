'''Considere uma equação do segundo grau, representada pela expressão

ax² + bx + c = 0

Construa um programa no qual o usuário informe os valores das constantes a, b e c.
Ao fim, o programa deve calcular e imprimir as raízes reais da equação.
Caso não existam raízes reais, o programa deve apresentar a mensagem "Não existem raízes reais".
Equação do segundo grau: '''
from math import sqrt
import math


print("Considere uma equação do segundo grau, representada pela expressão")
print("ax² + bx + c = 0")

a = int(input("Informe o valor de a: "))
print(f"Valor de a = {a}")

b = int(input("Informe o valor de b: "))
print(f"Valor de b = {b}")

c = int(input("Informe o valor de c: "))
print(f"Valor de c = {c}")

delta = b**2 - 4 * a * c

if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print(f"x1  x2 = {x:.2f}")
else:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print(f"Raízes: x1 = {x1}, x2 = {x2}")
    

