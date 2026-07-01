#Crie uma matriz 2x2 contendo os valores 1, 2, 3, 4 e exiba em tela.

matriz = [
    [1, 2],
    [3, 4]
]
a = 0 

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(matriz[l][c], end=" ")
    print() 
        