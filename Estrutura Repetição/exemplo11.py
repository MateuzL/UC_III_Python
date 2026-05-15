import random
n = [2, 4, 7, 1, 3, 5, 6]
random.shuffle(n)
n.sort()       #Ordenação Crescente
print(n)
n.sort(reverse=True)  #Ordenação Decrescente
print(n)

copia = list(n)   #Copiar lista
print(n)
print(copia)

n.clear()         #Clear para limpar os dados da lista.
print(n)