#Tupla com os perfis permitidos no sistema
perfis_permitidos = ("Aluno", "Professor", "Tecnico")

#Tupla com os tipos de problemas
tipos_problemas = ("Internet", "Computador", "Projetor", "Teclado", "Mouse")

#Lista armazena os usuários cadastrados no sistema
usuarios = []

#Lista que armazena os chamados
chamados = []

#Função para salvar os dados do arquivo em txt
def salvar_usuario_arquivo(usuario):
    
    #Tenta abrir e gravar no arquivo
    try:
        #Abre o arquivo
        arquivo = open('C:/Users/lucen/arquivospython/cadastro_usuario.txt', 'a', encoding='utf-8')  #encoding serve para ler o nome com acento
        
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
    
    #Retorna vazio
    return None
   
   
#Função para registrar chamados
def registrar_chamados(usuario_logado):
    
    #Cria um dicionário para armazenar o chamado
    chamado = {}
    
    chamado['usuario'] = usuario_logado['nome']
    
    print("Tipos de Problemas")
    
    for problema in tipos_problemas:
        
        print("-", problema)
        
    chamado["problema"] = input("Digite o tipo de problema: ")
    
    if chamado["problema"] not in tipos_problemas:
        
        print("Tipo de problema inválido")
        
        return
    
    chamado["descricao"] = input("Descreva o problema: ")
    
    chamado["status"] = "Aberto"
    
    chamados.append(chamado)
    
    salvar_chamado_arquivo(chamado)      
    
    
#Função para salvar chamado em arquivo
def salvar_chamado_arquivo(chamado):
    try:
        #Abre o arquivo
        arquivo_chamado = open('C:/Users/lucen/arquivospython/chamado_usuario.txt', 'a', encoding='utf-8')  #encoding serve para ler o nome com acento
        
        #Escreve os dados do usuário no arquivo txt separando por ;
        arquivo_chamado.write(
            chamado['usuario'] + ";" + 
            chamado['problema'] + ";" + 
            chamado['descricao'] + ";" +
            chamado['status'] + "\n"
        )
        
        #Fecha o arquivo
        arquivo_chamado.close()
        
    #Mostra o erro de gravação no arquivo    
    except:
        #Mostra a mensagem de erro de gravação
        print("Erro ao salvar o chamado no arquivo.")
        
    #Sempre vai exceutar    
    finally:
        #Mostra a mensagem de sucesso
        print("Chamado salvos com sucesso!!!")
        
        
def carregar_chamados():
    try:
        #Abre o arquivo txt no modo leitura "r"
        arquivo_chamado = open("C:/Users/lucen/arquivospython/chamado_usuario.txt", 'r', encoding='utf-8')
        
        #Percorre cada linha dentro do arquivo txt
        for linha in arquivo_chamado:
            
            #Remove espaços de linha com a função "strip()"
            linha = linha.strip()
            
            #Verifica se a linha não está vazia
            if linha != '':
                
                #Separa os dados usando ";"
                dados = linha.split(";")
                
                #Cria um dicionário para armazenar os dados do chamado
                chamado = {
                    "usuario": dados[0],
                    "problema": dados[1],
                    "descricao": dados[2],
                    "status": dados[3]
                }
                
                #Adiciona o chamado dentro da lista de chamados
                chamados.append(chamado)
             
        #Fecha o arquivo após leitura        
        arquivo_chamado.close()
        
    #Caso o arquivo ainda não exista, isso aqui vai funcionar    
    except FileNotFoundError:
        
        #Mostra a mensagem informando que nenhum usuario foi carregado
        print("O arquivo não foi criado ainda.")
        
    #Sempre irá executar    
    finally:
        #Mensagem para mostrar o carregamento de usuário
        print("Chamados carregados com Sucesso!")
        
    
    
            
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
   
   
#Essa função é responsável por carregar os usuários do arquivo txt   
def carregar_usuario():
    #Try para tentar abrir o arquivo txt
    try:
        #Abre o arquivo txt no modo leitura "r"
        arquivo = open("C:/Users/lucen/arquivospython/cadastro_usuario.txt", 'r', encoding='utf-8')
        
        #Percorre cada linha dentro do arquivo txt
        for linha in arquivo:
            
            #Remove espaços de linha com a função "strip()"
            linha = linha.strip()
            
            #Verifica se a linha não está vazia
            if linha != '':
                
                #Separa os dados usando ";"
                dados = linha.split(";")
                
                #Cria um dicionário para armazenar os dados do usuário
                usuario = {
                    "nome": dados[0],
                    "login": dados[1],
                    "senha": dados[2],
                    "perfil": dados[3]
                }
                
                #Adiciona o usuário dentro da lista de usuarios
                usuarios.append(usuario)
             
        #Fecha o arquivo após leitura        
        arquivo.close()
        
    #Caso o arquivo ainda não exista, isso aqui vai funcionar    
    except FileNotFoundError:
        
        #Mostra a mensagem informando que nenhum usuario foi carregado
        print("O arquivo não foi criado ainda.")
        
    #Sempre irá executar    
    finally:
        #Mensagem para mostrar o carregamento de usuário
        print("Usuário carregado com Sucesso!")
                
                
#Função para mostrar o menu após o login        
def menu_sistema(usuario_logado):
    
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
            registrar_chamados(usuario_logado)
        
        elif opcao == 2:
            #Verifica se não exite chamados
            if len(chamados) == 0:
                
                #Verifica se não existe usuário
                print("Nenhum chamado cadastrado.")
            
            #Caso existam usuários
            else:
                
                #Percorre a lista de usuarios
                for chamado in chamados:
                    
                    #Mostra o nome, login e perfil
                    print(
                        chamado['usuario'],
                        '-',
                        chamado['problema'],
                        '-',
                        chamado['descricao'],
                        '-',
                        chamado['status']
                        )
        
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
            #Chama a função fazer login
            usuario_logado = fazer_login()
            
            #Verifica se o login deu certo
            if usuario_logado != None:
                menu_sistema(usuario_logado)
            
        elif opcao == 3:
            
            #Verifica se não exite usuário
            if len(usuarios) == 0:
                
                #Verifica se não existe usuário
                print("Nenhum usuário cadastrado.")
            
            #Caso existam usuários
            else:
                
                #Percorre a lista de usuarios
                for usuario in usuarios:
                    
                    #Mostra o nome, login e perfil
                    print(usuario['nome'], '-', usuario['login'], '-', usuario['perfil'])
                
                
            
        elif opcao == 4:
            print("Saindo do sistema...")
            break
        
        else:
        #Mostra a mensagem de erro
            print("Opção inválida.")
            
carregar_usuario()
carregar_chamados()
menu_principal()       
     
    