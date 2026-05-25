'''Crie funções:

somar()
subtrair()
multiplicar()
dividir()

Depois faça um menu para escolher a operação.'''

def somar():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    soma = a + b
    print(f"A soma de {a} + {b} é : {soma}")
    
def subtrair():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    subtracao = a - b
    print(f"A subtração de {a} - {b} é: {subtracao}")
    
def multiplicar():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    multiplicacao = a * b
    print(f"A multiplicação de {a} x {b} é: {multiplicacao}")
    
def dividir():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    divisao = a / b
    print(f"A divisão de {a} / {b} é: {divisao}")
    
def menu():
    while True:
        print("======= Calculadora =======")
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
            print("Saindo da Calculadora...")
            break
        else:
            print("Opção inválida, tente novamente.")
        
menu()    
        
    
        
        