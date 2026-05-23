meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

while True:
    numero = int(input("Digite um número de 1 a 12: \n"))
    if 1 <= numero <= 12:
        print(meses[numero - 1])
    else:
        print("Número inválido. Por favor, digite um número de 1 a 12.")
        
    resposta = int(input("Deseja continuar? (1 - Sim, 2 - Não): \n"))
    if resposta == 2:
        break  
    
for i in range(12, 0, -1):
    print(meses[i - 1])
    
