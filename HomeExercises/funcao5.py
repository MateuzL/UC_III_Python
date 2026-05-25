'''
Crie uma função chamada cadastrar_produto().

Ela deve:

pedir:
nome do produto
preço
guardar em um dicionário
mostrar o dicionário no final

Exemplo:

{
    "nome": "Mouse",
    "preco": 50
}'''

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    
    produtos = {
        "nome": nome,
        "preco": preco
    }
    print(produtos)
    
cadastrar_produto()    
    
    
    
