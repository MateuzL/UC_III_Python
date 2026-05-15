import random
notas = [10, 8, 6, 4]
#random.shuffle(notas)
#notas.sort()   #Ordenação Crescente
print(notas)
menor = min(notas)
maior = max(notas)
print(f"A sua maior nota é: {maior}")

media = sum(notas) / len(notas)
print(f"A sua média é: {media}")