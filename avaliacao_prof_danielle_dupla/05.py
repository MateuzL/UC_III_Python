# Listas: Cadastre 5 nomes em uma lista e exiba todos os nomes cadastrados.

#Lista vazia para armazenar os nomes
lista = []

#For i range(5) porque são 5 nomes
for i in range(5):
    nome = input(f"Digite o {i+1}º Nome: ")
    lista.append(nome)     #Adicionando o nome na lista
    
print("Nomes cadastrados: ")
for nome in lista:         #Percorrendo a lista e imprimindo cada nome
    print("-", nome)
    