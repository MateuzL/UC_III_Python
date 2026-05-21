def soma(a, b):
    soma = a + b
    return soma


def subtracao(a, b):
    subtracao = a - b
    return subtracao


def multiplicacao(a, b):
    multiplicacao = a * b
    return multiplicacao


def divisao(a, b):
    divisao = a / b
    return divisao


def menu():
    print("Calculadora Simples")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    try:
        escolha = int(input("Digite o número da operação desejada: "))
        if escolha == 5:
            print("Saindo da calculadora...")
            return

        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))

        if escolha == 1:
            print(soma(a, b))
        elif escolha == 2:
            print(subtracao(a, b))
        elif escolha == 3:
            print(multiplicacao(a, b))
        elif escolha == 4:
            print(divisao(a, b))
        else:
            print("Opção inválida, tente novamente!")
            
    except ValueError:
        print("Erro! Por favor, digite apenas números.")
    finally:
        print("Finalizando...")
        
menu()        
       
        
