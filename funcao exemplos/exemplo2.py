'''FUNÇÃO PARA DESCOBRIR SE O NUMERO É PRIMO'''
def testar_primo(n):
    teste = 1
    for i in range(2, n):               #range 2 até n, (n) é o numero que queremos testar.
        if n % i == 0:
            teste = teste + 1
    if teste != 1:
        print("O número não é primo")
    else:
        print("O número é primo")
    
    
testar_primo(4)     #Para a função funcionar chamamos ela e passamos o número que queremos testar como argumento. No caso, estamos testando o número 4.