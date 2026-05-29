'''Crie uma função cadastrar_aluno() que:

peça:
nome
idade
2 notas
armazene tudo em um dicionário

Depois:

adicione o dicionário em uma lista
mostre todos os alunos cadastrados'''
cadastros = []
def cadastrar_aluno():
    while True:
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
    
        aluno = {
            "nome": nome,
            "idade": idade,
            "nota1": nota1,
            "nota2": nota2
        }
    
        cadastros.append(aluno)
        
        repetir = int(input("Deseja cadastrar outro aluno? 1 - SIM/2 - NAO"))
        if repetir == 2:
            break

cadastrar_aluno()
print("Alunos cadastrados: ")
for aluno in cadastros:
    print(f"Nome do aluno: {aluno["nome"]}")
    print(f"Idade: {aluno["idade"]}")
    print(f"Primeira nota: {aluno["nota1"]}")
    print(f"Segunda nota: {aluno["nota2"]}")
    print("======================")
       

    
    