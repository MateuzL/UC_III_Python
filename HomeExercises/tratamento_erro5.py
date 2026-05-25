'''Crie funções:

somar()
subtrair()
multiplicar()
dividir()

Depois faça um menu:

1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Sair
Regras
pedir 2 números
usar funções
usar while True
Tratamento de erro
Se digitar texto:
Digite apenas números!
Se dividir por zero:
Não é possível dividir por zero!'''

def somar():
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        resultado = a + b
        
        print(f"A soma de {a} + {b} é: {resultado}")
        
    except ValueError:
        print("Digite apenas números inteiros.")
        
def subtrair():
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        resultado = a - b
        
        print(f"A subtração de {a} - {b} é: {resultado}")
        
    except ValueError:
        print("Digite apenas números inteiros.")
        
def multiplicar():
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        resultado = a * b
        
        print(f"A multiplicação de {a} x {b} é: {resultado}")
        
    except ValueError:
        print("Digite apenas números inteiros.")
        
def dividir():
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        resultado = a / b
        
        print(f"A divisão de {a} por {b} é: {resultado}")
        
    except ValueError:
        print("Digite apenas números inteiros")
    except ZeroDivisionError:
        print("Não é possível dividir por 0")
        
        
def menu():
    while True:
        try:
            print("=====MENU=====")
            print("1 - Somar")
            print("2 - Subtrair")
            print("3 - Multiplicar")
            print("4 - Dividir")
            print("5 - Sair")
            
            opcao = int(input("Digite a opção correspondente: "))
            
            if opcao == 1:
                somar()
            elif opcao == 2:
                subtrair()
            elif opcao == 3:
                multiplicar()
            elif opcao == 4:
                dividir()
            elif opcao == 5:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida, tente novamente.")
                
        except ValueError:
            print("Digite apenas o número da sua opção.")  
            
menu()             