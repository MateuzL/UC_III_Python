# Descobrindo quantidade de caracteres
nome = input("Digite seu nome: ")

if len(nome) > 10:  # O len retorna o numero de caracteres na string
    print("Seu nome é grande, possui mais de 10 caracteres.")
else:
    print("Seu nome tem ", len(nome), " caracteres.")
