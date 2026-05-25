'''Crie um sistema com menu:

1 - Mostrar número aleatório
2 - Somar números
3 - Sair
Regras
Opção 1

Mostrar número aleatório.

Opção 2
pedir dois números
mostrar soma
Tratamento de erro

Se o usuário:

digitar letras
digitar opção inválida

mostrar mensagens de erro sem quebrar o programa.'''
import random

def numero_aleatorio():
    numero = random.randint(1, 100)
    print(f"O número aleatório gerado é: {numero}")
    
    
def somar():
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        resultado = a + b
        print(f"A soma de {a} + {b} é: {resultado}")
        
    except ValueError:
        print("Digite apenas números inteiros.")
        
def menu():
    while True:
        try:
            print("=====MENU=====")
            print("1 - Número Aleatório")
            print("2 - Somar ")
            print("3 - Sair")
            
            opcao = int(input("Digite a opção correspondente: "))
            
            if opcao == 1:
                numero_aleatorio()
                
            elif opcao == 2:
                somar()
                
            elif opcao == 3:
                print("Saindo do Sistema...")
                
            else:
                print("Opção inválida, tente novamente.") 
                
        except ValueError:
            print("Digite apenas o número da opção.")              
    
menu()    