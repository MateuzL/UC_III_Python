numero_secreto = 42
chute = int(input("Digite um número: \n"))


if (chute == numero_secreto):
    print("Parabéns! Você acertou o número.")
elif (chute > numero_secreto):
    print("Errado! O número secreto é menor do que o número digitado.")
else:
    print("Errado! O número secreto é maior do que o número digitado.")
    