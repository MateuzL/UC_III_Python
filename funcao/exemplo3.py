dados = [] #Lista Vazia
disciplinas = []


def cadastrar_aluno():
    nome = input("Informe o nome do aluno: ")
    idade = int(input("Informe a idade do aluno: "))
    sexo = input("F - Feminino, M - Masculino: ")
    dados.append([nome, idade, sexo])
    print("Aluno cadastrado com sucesso!")
    
def cadastrar_disciplinas():
    disciplina = input("Informe o nome da disciplina: ")
    ch = int(input("Informe a carga horária da disciplina: "))
    disciplinas.append([disciplina, ch])
    print("Disciplina cadastrada com sucesso!")
    
while True:
    print("===Ssitema Acadêmico===")
    print("1 - Cadastrar Aluno")
    print("2 - Cadastrar Disciplina")
    print("3 - Sair")
    op = int(input("Informe o que deseja: "))
    if op == 1:
        cadastrar_aluno()
    elif op == 2:
        cadastrar_disciplinas()
    elif op == 3:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente!")    
    
'''cadastrar_aluno()
cadastrar_disciplinas()'''      
 

'''nome = input("Informe o nome do aluno: ")
idade = int(input("Informe a idade do aluno: "))
sexo = input("F - Feminino, M - Masculino: ")
cadastrar(nome, idade, sexo)
print(dados) '''   