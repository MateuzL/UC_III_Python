#Solicite os valores de uma matriz 3x3 e calcule a soma de todos os elementos.

matriz = []

soma = 0

for l in range(3):
    nova = []
    for c in range(3):
        valor = float(input(f"Digite o valor de {l}x{c}: "))
        nova.append(valor)
    matriz.append(nova)
    
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(matriz[l][c], end=" ")
        soma = soma + matriz[l][c]
    print()
    
print(f"A soma de todos os elementos é: {soma}")
    
