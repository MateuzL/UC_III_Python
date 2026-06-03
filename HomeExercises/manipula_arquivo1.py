'''Exercício 2 - Sistema de Produtos

Objetivo: Treinar dicionários dentro de listas.

Menu:

1 - Cadastrar produto
2 - Listar produtos
3 - Sair

Cada produto deve possuir:

{
    "nome": "",
    "preco": 0
}

Funções:

cadastrar_produto()
listar_produtos()
menu()

Exemplo da saída:

Notebook - R$3500
Mouse - R$80'''


produtos = []


def cadastrar_produto():
    try:
        produto = {
            "nome": input("Digite o nome do produto: "),
            "preco": float(input("Digite o preço do produto: "))
        }
        
        produtos.append(produto)
        print("Produto cadastrado com sucesso.")
        
        
    except ValueError:
        print("Valor inválido.")
        
        
    
def listar_produtos():
    
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
    
    for produto in produtos:
        print(f"Nome do produto: {produto['nome']} - Preço: R${produto['preco']:.2f}")    



#Função MENU
def menu():
    while True:
        print("=====MENU=====")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Sair")
    
        try:
            opcao = int(input("Digite a opção correspondente: "))
        
            if opcao == 1:
                cadastrar_produto()
                
            elif opcao == 2:
                listar_produtos()
            
            elif opcao == 3:
                print("Saindo...")
                break
                
            else:
                print("Opção inválida, tente novamente")
                
        except ValueError:
            print("Digite apenas números.")
        
      
        
menu()                        