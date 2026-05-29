'''Faça um sistema que:
peça o nome do aluno
peça 3 notas
armazene as notas em uma lista
calcule a média
mostre:
Aprovado se média >= 7
Senão Reprovado'''

print("Sistema de Nota")
alunos = []
notas = []

nome = input("Digite o nome do aluno: ")
for i in range(3):
    nota = float(input(f"Digite a {i + 1}ª Nota: "))
    notas.append(nota)
    
#Calculando a média:

media = sum(notas) / len(notas)  

#Rsultado:

print(f"Nome do Aluno: {nome}")
print(f"Notas: {notas}")
print(f"Média: {media}")

if media >= 10:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado!")
    
  
  