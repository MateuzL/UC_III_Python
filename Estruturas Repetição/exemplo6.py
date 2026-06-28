pares = 0
impares = 0

for cont in range(5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1    
print(f"Quantidade de números pares digitados é: {pares}")
print(f"Quantidade de números ímpares digitados é: {impares}")      
      