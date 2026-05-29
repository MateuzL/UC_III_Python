'''Crie um sistema com menu:

1 - Olá
2 - Número aleatório
3 - Sair

Crie uma função para cada opção.

Exemplo:

def ola():
def numero_aleatorio():
def menu():

Use while True.'''
import random

def ola():
    print("Olá Usuário")
    
     
def numero_aleatorio():
    numero = random.randint(1, 100)
    print(f"Número aleatório: {numero}")
    
    
def menu():
    while True:
        print("=====Menu=====")
        print("1 - Olá")
        print("2 - Número aleatório")
        print("3 - Sair")
        
        opcao = int(input("Escolha a opção: "))
        
        if opcao == 1:
            ola()
        elif opcao == 2:
            numero_aleatorio()
        elif opcao == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente")
menu()            
        