# Estruturas de dados
alunos = []
notas = []

# Função para cadastrar aluno
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = input("Idade: ")
    turma = input("Turma: ")

    alunos.append({"nome": nome, "idade": idade, "turma": turma})
    notas.append([0, 0, 0, 0])

    print("Aluno cadastrado com sucesso!\n")


# Função para achar posição do aluno (sem index/enumerate)
def encontrar_posicao(nome):
    pos = 0
    for a in alunos:
        if a["nome"].lower() == nome.lower():
            return pos
        pos += 1
    return -1


# Função para lançar notas
def lancar_notas():
    nome = input("Nome do aluno: ")
    pos = encontrar_posicao(nome)

    if pos == -1:
        print("Aluno não encontrado.\n")
        return

    print("Lançando notas para", alunos[pos]["nome"])

    i = 0
    while i < 4:
        nota = float(input("Digite a nota " + str(i + 1) + ": "))
        if nota >= 0 and nota <= 10:
            notas[pos][i] = nota
            i += 1
        else:
            print("Nota inválida!")
    
    print("Notas lançadas com sucesso!\n")


# Função para calcular média
def calcular_media(pos):
    soma = 0
    i = 0
    while i < 4:
        soma += notas[pos][i]
        i += 1
    return soma / 4


# Função para consultar aluno
def consultar_aluno():
    nome = input("Nome do aluno: ")
    pos = encontrar_posicao(nome)

    if pos == -1:
        print("Aluno não encontrado.\n")
        return

    media = calcular_media(pos)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print("\n--- DADOS DO ALUNO ---")
    print("Nome:", alunos[pos]["nome"])
    print("Idade:", alunos[pos]["idade"])
    print("Turma:", alunos[pos]["turma"])
    print("Notas:", notas[pos])
    print("Média:", media)
    print("Situação:", situacao)
    print()


# Função para relatório geral
def relatorio_geral():
    total = len(alunos)

    if total == 0:
        print("Nenhum aluno cadastrado.\n")
        return

    soma_medias = 0
    melhor_media = -1
    pior_media = 11

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    nome_melhor = ""
    nome_pior = ""

    i = 0
    while i < total:
        media = calcular_media(i)
        soma_medias += media

        if media > melhor_media:
            melhor_media = media
            nome_melhor = alunos[i]["nome"]

        if media < pior_media:
            pior_media = media
            nome_pior = alunos[i]["nome"]

        if media >= 7:
            aprovados += 1
        elif media >= 5:
            recuperacao += 1
        else:
            reprovados += 1

        i += 1

    media_turma = soma_medias / total

    print("\n--- RELATÓRIO GERAL ---")
    print("Total de alunos:", total)
    print("Média da turma:", media_turma)
    print("Melhor aluno:", nome_melhor, "Média:", melhor_media)
    print("Pior aluno:", nome_pior, "Média:", pior_media)
    print("Aprovados:", aprovados)
    print("Recuperação:", recuperacao)
    print("Reprovados:", reprovados)
    print()


# Função para salvar dados em TXT (sem join)
def salvar_dados():
    arquivo = open("dados_escola.txt", "w")

    i = 0
    while i < len(alunos):
        media = calcular_media(i)

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        texto = ""
        texto += "Nome: " + alunos[i]["nome"]
        texto += ", Idade: " + alunos[i]["idade"]
        texto += ", Turma: " + alunos[i]["turma"]
        texto += ", Notas: "

        j = 0
        while j < 4:
            texto += str(notas[i][j])
            if j < 3:
                texto += " "
            j += 1

        texto += ", Média: " + str(media)
        texto += ", Situação: " + situacao + "\n"

        arquivo.write(texto)
        i += 1

    arquivo.close()
    print("Dados salvos com sucesso!\n")


# Menu principal
def menu():
    while True:
        print("=== SISTEMA ESCOLAR ===")
        print("1 - Cadastrar aluno")
        print("2 - Lançar notas")
        print("3 - Consultar aluno")
        print("4 - Relatório geral")
        print("5 - Salvar dados")
        print("6 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_aluno()
        elif op == "2":
            lancar_notas()
        elif op == "3":
            consultar_aluno()
        elif op == "4":
            relatorio_geral()
        elif op == "5":
            salvar_dados()
        elif op == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")


# Executar sistema
menu()