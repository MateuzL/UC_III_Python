'''Exercício 5 - Mini Sistema de Chamados

Objetivo: Preparação para projetos maiores.

Menu principal:

1 - Cadastrar usuário
2 - Login
3 - Sair

Após login:

1 - Abrir chamado
2 - Listar meus chamados
3 - Logout

Estruturas:

Usuário:

{
    "nome": "",
    "login": "",
    "senha": ""
}

Chamado:

{
    "usuario": "",
    "descricao": "",
    "status": "Aberto"
}

Funções:

cadastrar_usuario()
fazer_login()
abrir_chamado(usuario_logado)
listar_chamados(usuario_logado)
menu_principal()
menu_usuario(usuario_logado)

Observe que agora você terá:

usuario_logado = fazer_login()

menu_usuario(usuario_logado)

que é exatamente o conceito que está te confundindo hoje.'''
chamados = []

usuarios = []

def cadastrar_usuario():
    usuario = {
        "login": input("Digite seu login: "),
        "senha": input("Digite sua senha: ")
    }
        
    usuarios.append(usuario)
    print("Usuario cadastrado com sucesso.")
    
    
def fazer_login():
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:
            print("Login realizado com sucesso!")
            return usuario
        
    print("Usuário ou senha inválida.")
    return None        
        
        
def abrir_chamado(usuario_logado):
    chamado = {
        
        "usuario": usuario_logado['login'],
        "descricao": input("Digite a descricao do chamado"),
        "status": "Aberto"
        
    }
    
    chamados.append(chamado)
    
    print("Chamado registrado com sucesso.")
    
    
    
        
def menu_sistema(usuario_logado):
    while True:
        try:
            
            print("1. Abrir chamado")
            print("2. Listar chamados")
            print("3. Logout")   
            
            opcao = int(input("Digite a opção correspondente: "))
            
            if opcao == 1:
                abrir_chamado(usuario_logado)
                
            elif opcao == 2:
                print("F")
                
            elif opcao == 3:
                print("Saindo...")
                break
                
            else:
                print("Opção inválida, tente novamente.")
                
        except ValueError:
            print("Digite apenas números.")     
        
        
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
                    menu_sistema(usuario_logado)
                
            elif opcao == 3:
                print("Saindo...")
                break
            
            else:
                print("Opção inválida.")
                
        except ValueError:
            print("Digite apenas números.")
            
menu()            