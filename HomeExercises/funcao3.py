'''Crie uma função chamada somar() que:

peça dois números
some os números
mostre o resultado

Exemplo:

Resultado: 15'''

def somar():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))
    resultado = a + b
    print(f"Resultado da soma: {resultado}")
    
somar()    
