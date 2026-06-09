#Solicite os valores de uma matriz 3x3 e calcule a soma da diagonal principal.

matriz = []

for l in range(3):
    nova = []
    for c in range(3):
        valor = int(input(f"Digite o valor de {l} x {c} : "))
        nova.append(valor)
    matriz.append(nova)
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        
        print(matriz[l][c], end=' ')
    print()
    
print(f"Números da diagonal principal: {matriz[0][0]}, {matriz[1][1]} e {matriz[2][2]}.")
print(f"A soma da diagonal principal é: {matriz[0][0] + matriz [1][1] + matriz[2][2]}.")
        
        