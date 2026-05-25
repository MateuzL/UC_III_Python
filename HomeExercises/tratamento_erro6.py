'''Crie um menu:

1 - Adicionar fruta
2 - Mostrar frutas
3 - Mostrar fruta aleatória
4 - Sair
Regras
Função adicionar_fruta()
pedir fruta
adicionar em uma lista
Função mostrar_frutas()
usar for
mostrar:
todas frutas
primeira fruta
última fruta
Função fruta_aleatoria()

Mostrar uma fruta aleatória usando:

random.choice()'''

import random

frutas = []

def adicionar_fruta():
    try:
        fruta = input("Digite o nome da fruta: ")
        frutas.append(fruta)
        
    except ValueError:
        print("Digite apenas caracteres.")
        
adicionar_fruta()
print(frutas)                
    
    