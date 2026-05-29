"""CONSTRUA UM ALGORITMO QUE RECEBA O NOME E O PREÇO DE 5 MEDICAMENTOS DE UMA DROGARIA.
O PROGRAMA DEVE INFORMAR O NOME E O PREÇO DO MEDICAMENTO MAIS BARATO, BEM COMO A MÉDIA ARITMÉTICA DOS PREÇOS INFORMADOS."""

media_preco = 0
medicamento = input("Digite o nome do Medicamento: ")
preco = float(input("Digite o preço do Medicamento: "))
nome_medicamento = medicamento
menor_preco = preco
media_preco = media_preco + preco

for i in range(4):
    medicamento = input("Informe o nome do Medicamento: ")
    preco = float(input("Informe o preço: "))
    
    if preco < menor_preco:
        menor_preco = preco
        nome_medicamento = medicamento
        
    media_preco = media_preco + preco

media = media_preco / 5        
      
print(f"O {nome_medicamento} é o medicamento mais barato, custa R${menor_preco}")
print(f"Media dos preços é: {media}")

'''QUEM AGUARDAR PARA DOAR SANGUE'''