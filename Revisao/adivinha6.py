import random

total_de_tentativas = 0
total_pontos = 100

print("Jogo do adivinha")
print("Adivinhe o número secreto!!!")
print("Selecione o nível de difculdade: ")
print("(1) 10 Tentativas (2) 5 Tentativas (3) 3 Tentativas")
opcao = int(input("Defina o nível: "))

if (opcao == 1):
    total_de_tentativas = 10
    total_pontos = 100
elif (opcao == 2):
    total_de_tentativas = 5
    total_pontos = 100
else:
    total_de_tentativas = 3
    total_pontos = 100

numero_secreto = random.randint(1, 100)

for tentativa in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(tentativa, total_de_tentativas))
    print(f"Pontuação atual: {total_pontos}")
    chute = int(input("Digite um número: \n"))
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    
    if (acertou):
        print("Parabéns! Você acertou o número.")
        break
    elif (maior):
        print("Errado! O número secreto é menor do que o número digitado.")
        total_pontos = total_pontos - 10
        print(f"Você perdeu 10 pontos, pontuação: {total_pontos}")
    else:
        print("Errado! O número secreto é maior do que o número digitado.")
        total_pontos = total_pontos - 10
        print(f"Você perdeu 10 pontos, pontuação: {total_pontos}")
    
print("Fim do jogo!")
print(f"O número secreto é: {numero_secreto}")
print(f"Pontuação final: {total_pontos}")
        