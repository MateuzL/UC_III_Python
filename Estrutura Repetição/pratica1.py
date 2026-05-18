"""Sistema escolar para cadastrar o aluno.
Dados: Nome, Idade, Sexo, Série e as 4 notas.
No final do programa, deve imprimir os dados e a média de cada aluno cadastrado."""

dados = []

print("***Sistema Escolar***")
print("Cadastro de Aluno")

while True:
    print("Escolha a Disciplina e digite o número. ")
    while True:
        disciplina = int(input("[1] - MATEMATICA/ [2] - PORTUGUES/ [3] - GEOGRAFIA/ [4] - BIOLOGIA\n"))
        if disciplina == 1:
            disciplina = "Matemática"
            break
        elif disciplina == 2:
            disciplina = "Português"
            break
        elif disciplina == 3:
            disciplina = "Geografia"
            break
        elif disciplina == 4:
            disciplina = "Biologia"
            break
        else:
            print("Opção inválida, tente novamente.")
        
    print(f"Disciplina selecionada: {disciplina}")

    nome = input("Digite o Nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    while True:
        sexo = int(input("Digite o sexo do aluno: [1] - MASCULINO/ [2] - FEMININO\n"))
        if sexo == 1:
            sexo = "Masculino"
            break
        elif sexo == 2:
            sexo = "Feminino"
            break
        else:
            print("Opção inválida, tente novamente.")
            
    serie = input("Digite a série do aluno: ")

    print("Cadastre as notas: ")
    nota1 = float(input("Digite a Nota 1: "))
    nota2 = float(input("Digite a Nota 2: "))
    nota3 = float(input("Digite a Nota 3: "))
    nota4 = float(input("Digite a Nota 4: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    #Adicionando os dados em um dicionário

    aluno = {
        "disciplina": disciplina,
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "serie": serie,
        "notas": [nota1, nota2, nota3, nota4],
        "media": media,
    }
    dados.append(aluno)

    continuar = int(input("Deseja cadastrar outro aluno? [1] SIM [2] NAO\n"))
    if continuar == 2:
        break

print("===== LISTA DE ALUNOS =====")

for aluno in dados:
    #print(dados)
    print(f"\nDisciplina: {aluno['disciplina']}")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Sexo: {aluno['sexo']}")
    print(f"Série: {aluno['serie']}")
    print(f"Média: {aluno['media']:.2f}")
