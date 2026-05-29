#Tupla com os perfis permitidos no sistema
perfis_permitidos = ("Aluno", "Professor", "Tecnico")

#Lista armazena os usuários cadastrados no sistema
usuarios = []

#Função para salvar os dados do arquivo em txt
def salvar_usuario_arquivo(usuario):
    
    #Tenta abrir e gravar no arquivo
    try:
        #Abre o arquivo
        arquivo = open('C:/Users/vboxuser/Documents/cadastrado_usuario.txt', 'w', encoding='utf-8')  #encoding serve para ler o nome com acento
        
        #Escreve os dados do usuário no arquivo txt separando por ;
        arquivo.write(
            usuario["nome"] + ";" +
            usuario["login"] + ";" +
            usuario["senha"] + ";" +
            usuario["perfil"] + "\n"
        )
        
        #Fecha o arquivo
        arquivo.close()
        
    #Mostra o erro de gravação no arquivo    
    except:
        #Mostra a mensagem de erro de gravação
        print("Erro ao salvar os dados do usuário no arquivo.")
        
    #Sempre vai exceutar    
    finally:
        #Mostra a mensagem de sucesso
        print("Dados salvos com sucesso!!!")        

#Função para fazer login
def fazer_login():
    
    #Solicita os dados do login
    login = input("Digite seu Login: ")
    senha = input("Digite sua Senha: ")
    
    #Percorre a lista de usuários
    for usuario in usuarios:
        #Verifica se o login e a senha estão corretos
        if usuario['login'] == login and usuario['senha'] == senha:
            print("Login realizado com Sucesso!")
            return usuario
        
    #Mostra a mensagem caso nao encontre o usuario    
    print("***Login ou Senha incorreta!!!***")    

#Uma função para cadastrar novos usuários
def cadastrar_usuario():
    #Criar um dicionário vazio para o usuário
    usuario = {}
    #Solicita o nome completo do usuário e armazena no dicionário
    usuario['nome'] = input("Digite o nome completo: ")
    usuario['login'] = input("Digite o login: ")
    usuario['senha'] = input("Digite a senha: ")
    
    #Mostra os perfis do sistema
    print("\nPerfis disponíveis: ")
    
    #Percorre a tupla de perfis
    for perfil in perfis_permitidos:
        #Mostra cada perfil disponível
        print("-", perfil)
        
    #Solicita o perfil ao usuario    
    usuario["perfil"] = input("Escolha um perfil: ")
    
    #Verifica se o perfil escolhido pelo usuário é válido
    if usuario['perfil'] not in perfis_permitidos:
        print("Perfil inválido.")
        
        #Encerra a função cadastrar
        return
    
    #Percorre a lista de usuários já cadastrados
    for i in usuarios:
        
        #Verifica se o Login já existe
        if i['login'] == usuario['login']:
            
            #Mostra a mensagem de Erro
            print("Esse Login já existe.")
            #Encerrra a função
            return
        
    #Adiciona o usuário na lista    
    usuarios.append(usuario)
    
    salvar_usuario_arquivo(usuario)
    
    print("Usuário cadastrado com sucesso!")    
   
#Função para mostrar o menu após o login        
def menu_sistema():
    
    while True:
        
        #Mostra o Menu do sistema
        print("\n===== Menu Sistema =====")
        print("1. Registrar Chamado")
        print("2. Listar Chamados")
        print("3. Sair")
        
        try:
            opcao = int(input("Digite uma opção: "))
        except ValueError:
            print("Erro! Digite apenas números")
            continue
        
        finally:
            print("Opção processada com Sucesso.")
    
        if opcao == 1:
            print("Opção 1")
        
        elif opcao == 2:
            print("Opção 2")
        
        #Se esolher a 3, sai da conta    
        elif opcao == 3:
            print("Saindo da conta...")
            break
        
        else:
            print("Opção inválida.")
    
#Função Principal do Programa
def menu_principal():
    while True:
        print("==== SISTEMA DE CHAMADOS ESCOLAR ====")
        print("1. Cadastrar usuário")
        print("2. Fazer Login")
        print("3. Listar usuários cadastrados")
        print("4. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")
            continue  #Continuar o loop para solicitar a opção novamente
        
        #Sempre vai exeutar
        finally:                   
            #Mostra mensagem que a opçao deu certo
            print("Processamento concluído.")
            
        if opcao == 1:
            cadastrar_usuario()
            
        elif opcao == 2:
            usuario_logado = fazer_login()
            
        elif opcao == 3:
            print("opção 3")
            
        elif opcao == 4:
            print("Saindo do sistema...")
            break
        
        else:
        #Mostra a mensagem de erro
            print("Opção inválida.")
            
menu_principal()       
     
    