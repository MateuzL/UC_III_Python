#Solicite os valores de uma matriz de 3x3 e encontre o maior valor

matriz = []
maior = 0


for l in range(3):
    nova = []
    for c in range(3):
        valor = float(input(f"Digite o valor de {l} x {c} : "))
        nova.append(valor)
    matriz.append(nova)
    
for c in range(len(matriz)):
    for l in range(len(matriz[l])):
        if matriz[l][c] > maior:
            maior = matriz[l][c]
        
        
print(f"O maior valor da matriz é: {maior}")
        