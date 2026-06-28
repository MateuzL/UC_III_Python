# Matrizes: Crie uma matriz 3x3, solicite os valores, exiba a matriz, a soma dos elementos e a diagonal principal.

matriz = []
soma = 0

# Solicitando os valores da matriz
for l in range(3):
    linha = []
    for c in range(3):
        valor = float(input(f"Digite o valor de {l} x {c} : "))
        linha.append(valor)
    matriz.append(linha)
    
print("-*"*20)

# Exibindo a matriz
print("Matriz 3x3:")
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(matriz[l][c], end=' ')
        soma = soma + matriz[l][c]
    print()
    
#Exibindo a soma dos elementos
print(f"\nA soma dos elementos é: {soma}")

#Exibindo os valores da diagonal principal
print(f"Diagonal principal: {matriz[0][0]}, {matriz[1][1]} e {matriz[2][2]}.")

    

            
    