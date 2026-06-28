"""SISTEMA ESCOLAR CADASTRE ALUNO: NOME, IDADE, SEXO, SÉRIE.
CADASTRO DE DISCIPLINA
PROFESSOR LANÇA 4 NOTAS PARA O ALUNO E NO FINAL LISTE A NOTA DE CADA ALUNO / MEDIA

RELATORIO FINAL: IMPRIMIR NOME DO ALUNO, IDADE, SEXO E SÉRIE. A DISCIPLINA E A MÉDIA."""

import random

print("***Sistema Escolar***")

while True:
    aluno = {
        disciplina = input("Digite o nome da Disciplina: ")
        aluno["disciplina"] = disciplina
        
        nome = input("Digite o nome do aluno: \n")
        aluno["nome"] = nome
        idade = int(input("Digite a idade do aluno: \n"))
        aluno["idade"] = idade
        sexo = input("Digite o sexo do aluno: M - Masculino F - Feminino: \n")
        aluno["sexo"] = sexo
        serie = input("Digite a série do aluno: \n")
        aluno["serie"] = serie
        nota1 = int(input("Digite a nota 1: "))
        aluno["nota1"] = nota1
        nota2 = int(input("Digite a nota 2: "))
        aluno["nota2"] = nota2
        nota3 = int(input("Digite a nota 3: "))
        aluno["nota3"] = nota3
        nota4 = int(input("Digite a nota 4: "))
        aluno["nota4"] = nota4
        media = (nota1 + nota2 + nota3 + nota4) / 4
    }

    repetir = int(input("Deseja adicionar mais um cadastro? 1 - SIM OU 0 - NAO"))
    if repetir == 0:
        break
    
    
#print(aluno.keys())
#print(aluno.items())
print(aluno.values())
print(f"Média: {media}")
