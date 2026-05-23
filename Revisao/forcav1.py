print("*"*20)
print("*"*5, 'Bem vindo ao Jogo da Forca', "*"*5)
print("*"*20)

palavra_secreta = 'banana'
letras_acertadas = ['_', '_','_','_','_','_']


acertou = False
enforcou = False
erros = 0

while (not acertou and not enforcou):
    chute = input('Qual a Letra? \n').upper()
    
    if (chute in palavra_secreta.upper()):
        posicao = 0
        for letra in palavra_secreta:
            if (chute == letra.upper()):
                #print('Encontrei a letra {} na posição {}'.format(letra, posicao))
                letras_acertadas[posicao] = letra

            posicao = posicao + 1
    else:
        erros = erros + 1
        
    enforcou = erros == 5
    acertou = '_' not in letras_acertadas    
    print(letras_acertadas)
    
if (acertou):
    print('Parabéns, você ganhou!')
else:
    print('Você foi enforcado!')    

print('Fim de Jogo')