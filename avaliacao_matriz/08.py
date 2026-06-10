#Solicite os valores de uma matriz 4x4 e informe quantos números pares existem.

matriz = []
pares = 0

for l in range(4):
    linha = []
    for c in range(4):
        valor = int(input(f"Digite o valor de {l} x {c} : "))
        linha.append(valor)
    matriz.append(linha)
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        
        print(matriz[l][c])
        
        if matriz[l][c] % 2 == 0:
            pares = pares + 1
            
print(f"A quantidade de números pares nessa matriz é: {pares}")
        