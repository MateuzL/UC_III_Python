''' Desenvolva um Sistema de Gerenciamento Escolar contendo as seguintes funcionalidades: 
- Menu principal com as opções: Cadastrar Aluno, Lançar Notas, Consultar Aluno, Relatório geral, Salvar Dados e sair.
- Cadastro de alunos contendo nome, idade e turma.
- Lançamento de quatro notas por aluno.
- Consulta individual contendo dados do aluno, média e situação.
- Relatório geral contendo quantidade de alunos, média da turma, melhor aluno, pior aluno, aprovados, recuperação e reprovados.
- Salvar os dados em arquivo TXT.
- Implementar uma matriz de notas onde cada linha representa um aluno e cada coluna representa uma nota,
calculando automaticamente a média dos alunos.'''

def menu():
    while True:
        try:
            print("===== Gerenciamento Escolar =====")
            print("1 - Cadastrar Aluno")
            print("2 - Lançar Notas")
            print("3 - Consulta Aluno")
            print("4 - Relatório Geral")
            print("5 - Salvar Dados")
            print("6 - Sair")
            
            op = int(input("Digite a opção correspondente: "))
            
        except ValueError:
            print("Opção inválida, por favor, digite um número.")
            
            