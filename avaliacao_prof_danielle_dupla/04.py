# Estrutura de repetição (While): Solicite números até que o usuário digite 0. Exiba quantidade e soma.
contador = 0
soma = 0

print("Digite números, quando quiser parar digite 0.")
while True:
    num = int(input("Digite um número: "))
    soma = soma + num
    contador = contador + 1
    
    if num == 0:
        break
    
print(f"Quantidade de números digitados: {contador-1}")
print(f"A soma dos números digitados é: {soma}")

    
    