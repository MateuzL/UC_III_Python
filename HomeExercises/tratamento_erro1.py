'''Tratamento de Erro'''

try:
    numero = int(input("Digite um número: "))
    print(numero)
    
except:
    print("Digite apenas numeros inteiros.")