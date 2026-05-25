'''Controle de Estoque simples
Crie um produto:
produto = {
    "nome": "Teclado",
    "estoque": 10
}
O sistema deve perguntar:

Quantos itens deseja retirar?

Depois:

diminuir do estoque
mostrar o estoque atualizado

Se tentar retirar mais do que existe:

Estoque insuficiente'''

print("Controle de Estoque")

produto = {
    "nome": "Teclado",
    "estoque": 10
}


print(f"Nome do produto: {produto["nome"]}")
print(f"Estoque: {produto["estoque"]}")

retirada = int(input("Quantos itens deseja retirar? "))

if retirada <= produto["estoque"]:
    produto["estoque"] = produto["estoque"] - retirada
else:
    print("Quantidade maior que o estoque.")
    
print(f"Nome do Produto: {produto["nome"]}")
print(f"Estoque: {produto["estoque"]}")

    
    