# Estrutura de Repetição (For): Solicite 5 números e apresente soma e média.

# Variaveis (soma) e (media) para armazenar seus respectivos valores
soma = 0
media = 0

# Solicitando 5 números
for i in range(5):
    numero = int(input(f"Digite o {i+1}º Número: "))
    soma = soma + numero
    
media = soma / (i+1)    

# Imprimindo a soma e a média
print(f"A soma dos número digitados é: {soma}")    
print(f"A Média da soma é: {media}")

