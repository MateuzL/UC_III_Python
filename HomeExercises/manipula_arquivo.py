'''Exercício 1 - Cadastro de Nomes

Objetivo: Treinar funções e listas.

Crie um menu:

1 - Adicionar nome
2 - Mostrar nomes
3 - Sair

Funções obrigatórias:

adicionar_nome()
mostrar_nomes()
menu()

Regras:

Os nomes devem ser armazenados em uma lista.
Mostrar todos os nomes usando for.
Tratar erro caso o usuário digite letra no menu.'''

nomes = []
#Função para adicionar nomes
def adicionar_nome():
    
    nome = input("Digite o nome a ser adicionado: ")
    
    nomes.append(nome)
    print("Nome adicionado com sucesso.")
    return
    
    
def mostrar_nomes():
    
    if len(nomes) == 0:
        print("Nenhum nome adicionado.")
        return
    
    for nome in nomes:
        print(nome)    
    
    
#Função MENU
def menu():
    while True:
        print("=====MENU=====")
        print("1. Adicionar nome")
        print("2. Mostrar nomes")
        print("3. Sair")
        try:
            opcao = int(input("Digite a opção correspondente: "))
        
            if opcao == 1:
                adicionar_nome()
            elif opcao == 2:
                mostrar_nomes()
            elif opcao == 3:
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente")
            
        except ValueError:
            print("Digite apenas números.")
            
            
menu()