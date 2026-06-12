''' Desenvolva um Sistema de Gerenciamento Escolar contendo as seguintes funcionalidades: 
- Menu principal com as opções: Cadastrar Aluno, Lançar Notas, Consultar Aluno, Relatório geral, Salvar Dados e sair.
- Cadastro de alunos contendo nome, idade e turma.
- Lançamento de quatro notas por aluno.
- Consulta individual contendo dados do aluno, média e situação.
- Relatório geral contendo quantidade de alunos, média da turma, melhor aluno, pior aluno, aprovados, recuperação e reprovados.
- Salvar os dados em arquivo TXT.
- Implementar uma matriz de notas onde cada linha representa um aluno e cada coluna representa uma nota,
calculando automaticamente a média dos alunos.'''


alunos = []
matriz_notas = []


# Função para cadastrar aluno
def cadastrar_aluno():
    print("===CADASTRO DE ALUNO===")
    
    aluno = {
        "nome": input("Digite o nome do aluno: ").title(),
        "idade": int(input("Digite a idade do aluno: ")),
        "turma": input("Digite a turma: "),
        "notas": [0, 0, 0, 0]
    }
    
    alunos.append(aluno)
    matriz_notas.append([0, 0, 0, 0])
    print("Aluno cadastrado com sucesso.")
    
    
# Função lançar notas   
def lancar_notas():
    print("===LANÇAMENTO DE NOTAS===")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    
    i = 1

    for aluno in alunos:
        print(f"{i} - {aluno['nome']}")
        i += 1   
    
    indice = int(input("Escolha o aluno: ")) - 1
    
    if indice < 0 or indice >= len(alunos):
        print("Aluno inválido.\n")
        return
    
    notas = []
    
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª Nota: "))
        notas.append(nota)
        
    alunos[indice]["notas"] = notas
    
    matriz_notas[indice] = notas
    #print(matriz_notas)
    print("Notas cadastradas com sucesso!")
    

# Função para calcular a média    
def calcular_media(linha_matriz):
    return sum(linha_matriz) / len(linha_matriz)
    
# Função condicional para a situação da média
def situacao(media):
    if media >= 7:
        return "APROVADO!"
    
    elif media >= 5:
        return "RECUPERAÇÃO!"
    
    else:
        return "REPROVADO!"

# Função para consultar um determinado aluno
def consultar_aluno():
    print("===CONSULTAR ALUNO===")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    
    i = 1

    for aluno in alunos:
        print(f"{i} - {aluno['nome']}")
        i += 1
        
    indice = int(input("Escolha o aluno: ")) - 1
    
    if indice < 0 or indice >= len(alunos):
            print("Aluno inválido.\n")
            return
        
    aluno = alunos[indice]
    
    media = calcular_media(matriz_notas[indice])
    
    print("\n--- Dados do Aluno ---")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Turma: {aluno['turma']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao(media)}\n")
    
    
def relatorio_geral():
    print("===RELATÓRIO GERAL===")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    
    medias = []

    for linha in matriz_notas:
        medias.append(calcular_media(linha))
    
    total_alunos = len(alunos)
    media_turma = sum(medias) / total_alunos
    melhor_aluno = alunos[0]["nome"]
    pior_aluno = alunos[0]["nome"]

    maior_media = medias[0]
    menor_media = medias[0]

    for i in range(len(medias)):
        if medias[i] > maior_media:
            maior_media = medias[i]
            melhor_aluno = alunos[i]["nome"]

        if medias[i] < menor_media:
            menor_media = medias[i]
            pior_aluno = alunos[i]["nome"]
    
    aprovados = sum(1 for m in medias if m >= 7)
    recuperacao = sum(1 for m in medias if 5 <= m < 7)
    reprovados = sum(1 for m in medias if m < 5)
    
    print("=== RELATÓRIO GERAL ===")
    print("-"*20)
    
    print(f"Total de alunos: {total_alunos}")
    print(f"Média dos alunos: {media_turma:.2f}")
    print(f"Melhor aluno: {melhor_aluno} com média: {maior_media:.2f}")
    print(f"Pior aluno: {pior_aluno} com média: {menor_media:.2f}")
    print(f"Aprovados: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}\n")
    
    
    
    
def salvar_dados():
    with open("c:/Users/vboxuser/Documents/gerenciamento_escolar.txt", 'w', encoding='utf-8') as arquivo:
        i = 0

        for aluno in alunos:
            media = calcular_media(matriz_notas[i])

            arquivo.write(f"Nome: {aluno['nome']}\n")
            arquivo.write(f"Idade: {aluno['idade']}\n")
            arquivo.write(f"Turma: {aluno['turma']}\n")
            arquivo.write(f"Notas: {aluno['notas']}\n")
            arquivo.write(f"Média: {media:.2f}\n")
            arquivo.write(f"Situação: {situacao(media)}\n")
            arquivo.write("=" * 30 + "\n")

            i += 1
    
    print("Dados salvos com sucesso no arquivo 'gerenciamento_escolar.txt'.\n")
    
    
# Função Menu
def menu():
    while True:
        try:
            print("===== Gerenciamento Escolar =====")
            print("1 - Cadastrar Aluno")
            print("2 - Lançar Notas")
            print("3 - Consultar Aluno")
            print("4 - Relatório Geral")
            print("5 - Salvar Dados")
            print("6 - Sair")
            
            op = int(input("Digite a opção correspondente: "))
            
        
            if op == 1:
                cadastrar_aluno()
                
            elif op == 2:
                lancar_notas()
                
            elif op == 3:
                consultar_aluno()
                
            elif op == 4:
                relatorio_geral()
                
            elif op == 5:
                salvar_dados()
                
            elif op == 6:
                print("Saindo do sistema...")
                break
            
            else:
                print("Opção inválida, tente novamente.")
                
        except ValueError:
            print("Opção inválida, por favor, digite um número.")
                
                
                
menu()
            