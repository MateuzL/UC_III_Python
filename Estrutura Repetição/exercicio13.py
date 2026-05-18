"""SISTEMA ESCOLAR CADASTRE ALUNO: NOME, IDADE, SEXO, SÉRIE.
CADASTRO DE DISCIPLINA
PROFESSOR LANÇA 4 NOTAS PARA O ALUNO E NO FINAL LISTE A NOTA DE CADA ALUNO / MEDIA

RELATORIO FINAL: IMPRIMIR NOME DO ALUNO, IDADE, SEXO E SÉRIE. A DISCIPLINA E A MÉDIA."""

dados = []

print("*** SISTEMA ESCOLAR ***")

while True:
    print("Cadastro de aluno")
    disciplina = int(input("Digite a disciplina: 1 - Matemática, 2 - Português, 3 - História: "))
    
    if disciplina == 1:
        disciplina = "Matemática"
    elif disciplina == 2:
        disciplina = "Português"
    elif disciplina == 3:
        disciplina = "História"
        
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    sexo = input("Digite o sexo do aluno: ")
    serie = input("Digite a série do aluno: ")

    print("\nDigite as 4 notas do aluno")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    #Adicionando os dados em um dicionário
    aluno = {
        "disciplina": disciplina,
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "serie": serie,
        #"notas": [nota1, nota2, nota3, nota4],
        "media": media
    }

    dados.append(aluno)

    continuar = input("\nDeseja cadastrar outro aluno? [S][N]): ").upper()     #Upper para converter a resposta para maiúscula
    if continuar != "S":
        break

# Exibindo os resultados
print("\n===== LISTA DE ALUNOS =====")
#print(dados)
print(dados)

'''for aluno in dados:
    print(f"\nDisciplina: {aluno['disciplina']}")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Sexo: {aluno['sexo']}")
    print(f"Série: {aluno['serie']}")
    #print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")'''