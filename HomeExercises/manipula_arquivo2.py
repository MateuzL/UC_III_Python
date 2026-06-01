'''Exercício 3 - Login Simples

Objetivo: Treinar retorno de função.

Cadastre usuários em uma lista.

Estrutura:

{
    "login": "",
    "senha": ""
}

Funções:

cadastrar_usuario()
fazer_login()
menu()

O diferencial:

A função fazer_login() deve retornar:

return usuario

ou

return None

Depois faça:

usuario_logado = fazer_login()

e mostre:

Bem-vindo João

Esse exercício é justamente para treinar o que te confundiu recentemente.'''

usuarios = []

def fazer_login():
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:
            print("Login realizado com Sucesso.")
            return usuario
        
    print("Usuário ou senha incorreta.")
    return None    



def cadastrar_usuario():
    
    usuario = {
        "login": input("Digite o login: "),
        "senha": input("Digite a senha: ")
    }
    
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")
    


def menu():
    while True:
        try:
            
            print("=====MENU=====")
            print("1. Cadastrar usuário")
            print("2. Fazer login")
            print("3. Sair")
            
            opcao = int(input("Digite a opção correspondente: "))
            
            if opcao == 1:
                cadastrar_usuario()
                
            elif opcao == 2:
                usuario_logado = fazer_login()
                
                if usuario_logado != None:
                    print(f"Bem vindo {usuario_logado['login']}")
                
            elif opcao == 3:
                print("Saindo...")
                break
                
            else:
                print("Opção inválida, tente novamente.")
                
        except ValueError:
            print("Digite apenas números.")
        
        
        
menu()        