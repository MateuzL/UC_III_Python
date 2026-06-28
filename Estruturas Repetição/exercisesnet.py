'''Exercício 1 — Lista simples

Crie uma lista vazia chamada nomes.

Peça 3 nomes ao usuário usando for.

Adicione os nomes na lista usando .append().

Depois imprima a lista completa.'''

nomes = []

for i in range(3):
    nome = input(f"Digite o {i+1} nome: ")
    nomes.append(nome)
print(nomes)

numeros = []

for j in range(5):
    numero = int(input(f"Digite o {j+1}ª Número: "))
    numeros.append(numero)
print(numeros)
soma = sum(numeros)
print(soma)
media = soma / 4
print(media)      

pessoa = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: ")),
    "cidade": input("Digite sua cidade: ")
}

print("Dados da pessoa registrada: ")
print(pessoa)





