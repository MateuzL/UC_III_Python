import random
nomes = []
while True:
    nome = input("Digite um nome: ")
    nomes.append(nome)               #append para adicionar o nome na lista
    
    op = input("Deseja continuar [S][N]?")
    if op.upper() == "N":            #upper para transformar minusculo em maiusculo
        break
print(nomes) 

random.shuffle(nomes)                #random.shuffle para embaralhar
print(f"Lista embaralhada: {nomes}")

sorteio = random.choice(nomes)       #random.choice para sortear um dado aleatório
print(f"O nome do sortudo é: {sorteio}")

while True:
    sorteio_2 = int(input("Deseja realizar novo sorteio? 1 - SIM OU 0 - NAO \n"))
    if sorteio_2 == 1:
        nomes.remove(sorteio)
        print(nomes)
        sorteio = random.choice(nomes)
        print(f"O nome do sortudo é: {sorteio}")
    else:
        print("Fim do sorteio.")
        break

