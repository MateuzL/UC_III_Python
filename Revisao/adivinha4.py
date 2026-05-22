'''x = 5

while (x > 1):
    print(x)
    x = x - 1'''
    
numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
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
        
    rodada = rodada + 1
    
print("Fim do jogo!")
    