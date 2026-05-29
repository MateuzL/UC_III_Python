'''Exercício 1 — Cadastro de Produtos

Crie um sistema que:

cadastre produtos
cada produto deve ter:
nome
categoria
preço
quantidade em estoque
armazene os produtos em uma lista
use dicionário para cada produto
tenha menu com:
cadastrar produto
listar produtos
sair
use try/except para preço e quantidade'''

produtos = []

nome_produto = input("Digite o nome do produto: ")
try:
    preco = int(input(f"Digite o preço do produto {nome_produto}: "))
    qtd_estoque = int(input(f"Digite a quantidade de estoque do produto {nome_produto}: "))
except:
    print("Digite apenas números.")
    
while True:
    print("Categoria do produto: ")
    print("1 - Smarthphone")
    print("2. Automóvel")
    print("3. Eletrodoméstico")
    while True:
        categoria = int(input("Digite a opção correspondente: "))
        if categoria == 1:
            categoria = "Smarthphone"
            break
        elif categoria == 2:
            categoria = "Automóvel"
            break
        elif categoria ==3:
            categoria = "Eletrodoméstico"
            break
        else:
            print("Opção inválida, tente novamente.")
    
    break

print("Produto Cadastrado com Sucesso!")
produto = {
    "nome_produto": nome_produto,
    "preco": preco,
    "estoque": qtd_estoque,
    "categoria": categoria
}

produtos.append(produto)

for produto in produtos:
    print(f"Produto: {produto['nome_produto']}")