'''Exercício 4 - Biblioteca

Objetivo: Treinar várias funções trabalhando juntas.

Menu:

1 - Cadastrar livro
2 - Emprestar livro
3 - Listar livros
4 - Sair

Estrutura:

{
    "titulo": "",
    "emprestado": False
}

Funções:

cadastrar_livro()
listar_livros()
emprestar_livro()
menu()

Fluxo:

menu()
   ↓
emprestar_livro()
   ↓
altera o dicionário

Aqui você começa a perceber como uma função modifica dados usados por outra'''
livros = []

def cadastrar_livro():
    livro = {
        "titulo": input("Digite o nome do livro: "),
        "emprestado": False
    }
    
    livros.append(livro)
    print("Livro cadastrado com sucesso.")
    
    
    

def listar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        
        for livro in livros:
            if livro["emprestado"]:
                status = "Sim"
            else:
                status = "Não"

            print(f"Título: {livro['titulo']} - Emprestado: {status}")    
        
        
 
def emprestar_livro():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return
        
    else:
        for i, livro in enumerate(livros):
            print(i + 1, "-", livro['titulo'])
            
    try:
        numero = int(input("Digite a opção correspondente ao livro desejado: "))
        if numero < 1 or numero > len(livros):
            print("Livro inválido.")
            return
    
        if livros[numero - 1]["emprestado"]:
            print("Este livro já está emprestado.")
            return
    
        livros[numero - 1]["emprestado"] = True 
        print("Livro emprestado com sucesso.")
    
    except ValueError:
        print("Digite apenas números.")
                
                
            
            
        
        
        
        
def menu():
    while True:
        
        print("=====MENU=====")
        print("1. Cadastrar livro")
        print("2. Emprestar livro")
        print("3. Listar livros")
        print("4. Sair")
        
        try:
            opcao = int(input("Digite a opção correspondente: "))
            
            if opcao == 1:
                cadastrar_livro()
                
            elif opcao == 2:
                emprestar_livro()
                
            elif opcao == 3:
                listar_livros()
                
            elif opcao == 4:
                print("Saindo...")
                break
            
            else:
                print("Opção inválida, tente novamente.")
                
        except ValueError:
            print("Digite apenas números.")
            
            
menu()            