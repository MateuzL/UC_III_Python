'''Menu Simples
Faça um menu:
1 - Olá
2 - Mostrar número
3 - Sair
Regras
Se escolher 1:

mostrar:

Olá usuário
Se escolher 2:

mostrar um número aleatório usando random

Se escolher 3:

encerrar sistema'''
import random
def menu():
    print("Menu")
    print("1 - Olá")
    print("2 - Mostrar Número aletório")
    print("3 - Sair.")
    
menu()

op = int(input("Digite a opção: "))

if op == 1:
    print("Olá Usuário")
elif op == 2:
    numero = random.randint(1,100)
    print(f"Número Aleatório: {numero}")
elif op == 3:
    print("Encerrando Sistema...")