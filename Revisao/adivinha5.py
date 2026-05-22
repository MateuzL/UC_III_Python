'''for x in range(1, 10, 2):
    print(x)'''
    
numero_secreto = 42
total_de_tentativas = 3
rodada = 1

for tentativa in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(tentativa, total_de_tentativas))
    chute = int(input("Digite um número: \n"))
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    
    if (acertou):
        print("Parabéns! Você acertou o número.")
        break
    elif (maior):
        print("Errado! O número secreto é menor do que o número digitado.")
    else:
        print("Errado! O número secreto é maior do que o número digitado.")
    
print("Fim do jogo!")
        