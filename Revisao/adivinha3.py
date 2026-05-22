numero_secreto = 42
chute = int(input("Digite um número: \n"))

acertou = chute == numero_secreto
maior = chute > numero_secreto


if (acertou):
    print("Parabéns! Você acertou o número.")
elif (maior):
    print("Errado! O número secreto é menor do que o número digitado.")
else:
    print("Errado! O número secreto é maior do que o número digitado.")
    