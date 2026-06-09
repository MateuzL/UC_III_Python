#Solicite ao usuário os valores de uma matriz 3x3, ao final exibba a matriz completa

matriz = []

for l in range(3):
    nova = []
    for c in range(3):
        valor = float(input(f"Digite o valor de {l}x{c}: "))
        nova.append(valor)
    matriz.append(nova)
    
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        
        print(matriz[l][c], end=" ")
    print()