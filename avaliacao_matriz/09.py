#Solicite os valores de uma matriz 3x3 e calcule a média dos elementos.

matriz = []
soma = 0



for l in range(3):
    linha = []
    for c in range(3):
        valor = int(input(f"Digite o valor para {l} x {c} : "))
        linha.append(valor)
    matriz.append(linha)
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        soma = soma + matriz[l][c]
        
        print(matriz[l][c], end=" ")
    print()
    
#media = soma / 9 
print(f"A soma de todos os elementos é: {soma}, portanto, a média é: {soma / (len(matriz) * len(matriz[0])):.2f}.")
        