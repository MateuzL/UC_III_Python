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

# Função para cadastrar aluno
def cadastrar_aluno():
    print("===CADASTRO DE ALUNO===")
    
    aluno = {
        "nome": input("Digite o nome do aluno: "),
        "idade": int(input("Digite a idade do aluno: ")),
        "turma": input("Digite a turma: "),
        "notas": [0, 0, 0, 0]
    }
    alunos.append(aluno)
    print(alunos)
    print("Aluno cadastrado com sucesso.")
    
    
# Função lançar notas   
def lancar_notas():
    print("===LANÇAMENTO DE NOTAS===")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    
    for i, aluno in enumerate(alunos):
        print(f"{i + 1} - {aluno['nome']}")   
    
    indice = int(input("Escolha o aluno: ")) - 1
    
    if indice < 0 or indice >= len(alunos):
        print("Aluno inválido.\n")
        return
    
    notas = []
    
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª Nota: "))
        notas.append(nota)
        
    alunos[indice]["notas"] = notas
    
    print(alunos)
    
    print("Notas cadastradas com sucesso!")
    

# Função para calcular a média    
def calcular_media(notas):
    return sum(notas) / len(notas)
    
# Função condiocional para a situação da média
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
    
    for i, aluno in enumerate(alunos):
        print(f"{i+1} - {aluno['nome']}")
        
    indice = int(input("Escolha o aluno: ")) - 1
    
    if indice < 0 or indice >= len(alunos):
            print("Aluno inválido.\n")
            return
        
    aluno = alunos[indice]
    media = calcular_media(aluno["notas"])
    
    print("\n--- Dados do Aluno ---")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Turma: {aluno['turma']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao(media)}\n")
    
    
'''def relatorio_geral():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    
    medias = [calcular_media(a["notas"]) for a in alunos]'''
    
    
    
    
'''def salvar_dados():
    arquivo = open("C:/Users/Documents/gerenciamento_escolar.txt", 'w', encoding='utf-8')
    
    arquivo.write(
        
    )
     
     
    arquivo.close()'''
    
    
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
                print("relatorio_geral()")
                
            elif op == 5:
                print("salvar_dados()")
                
            elif op == 6:
                print("Saindo do sistema...")
                break
            
            else:
                print("Opção inválida, tente novamente.")
                
        except ValueError:
            print("Opção inválida, por favor, digite um número.")
                
                
                
menu()
            