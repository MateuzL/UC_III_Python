'''Crie uma função chamada verificar_idade() que:

peça a idade do usuário
mostre:
"Maior de idade" se idade >= 18
"Menor de idade" caso contrário'''

def verificar_idade():
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")
        
verificar_idade()            