'''Crie uma função chamada mostrar_numero() que:

gere um número aleatório de 1 a 10
mostre o número na tela

Use random.'''

import random

def mostrar_numero():
    numero = random.randint(1, 10)
    print(numero)
    
mostrar_numero()    