numero_secreto = 42
chute = int(input("Digite um número: \n"))

while True:
    if (chute == numero_secreto):
        print("Parabéns! Você acertou o número.")
    else:
        if (chute > numero_secreto):
            print("Errado! O número secreto é menor do que o número digitado.")
        else:
            print("Errado! O número secreto é maior do que o número digitado.")