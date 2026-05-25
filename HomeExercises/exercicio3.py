'''Faça um sistema que:

cadastre 3 produtos com:

nome
preço

Cada produto deve ser um dicionário.

Depois mostre todos os produtos.'''

lista_produtos = []

print("Cadastro de Produtos")
print("Cadastre com nome e preço 3 produtos:")
for i in range(3):
    produto = input(f"Digite o nome do {i + 1} produto: ")
    preco = float(input(f"Digite o preço: "))
    
    produtos = {
        "nome": produto,
        "preco": preco
    }
    
    lista_produtos.append(produtos)
    
print(lista_produtos)


for produtos in lista_produtos:
    print("===============================")
    print(f"Nome do Produto: {produtos["nome"]}")
    print(f"Preço R$ {produtos["preco"]}")
        
    