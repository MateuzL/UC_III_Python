'''Sistema de Login
Faça um sistema com:
usuario_correto = "admin"
senha_correta = "1234"

O sistema deve:

pedir usuário
pedir senha
repetir até acertar
Quando acertar:

Login realizado com sucesso'''

usuario_correto = "admin"
senha_correta = "1234"

print("Sistema de Login")

while True:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Login Realizado com Sucesso!")
        break
    else:
        print("Login ou Senha inválido. Tente novamente.")
