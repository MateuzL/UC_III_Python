senha = input("Informe sua senha: ")
numeros = int(input("Possui números? 1 - SIM OU 0 - NAO"))
letra = int(input("Possui letras maiuscula? 1 - SIM OU  - NAO"))

if len(senha) > 8 and numeros == 1 and letra == 1:
    print("Senha forte.")
elif len(senha) > 8 and numeros == 1:
    print("Senha média.")
else:
    print("Senha fraca!")
