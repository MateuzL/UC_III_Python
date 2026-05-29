'''Faça um sistema que:
peça 5 nomes
armazene os nomes em uma lista
depois mostre todos os nomes cadastrados'''

nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1} nome: ")
    nomes.append(nome)

for nome in nomes:
    print(f"Nome: {nome}")    