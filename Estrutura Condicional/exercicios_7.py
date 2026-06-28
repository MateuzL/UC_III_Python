'''Uma imobiliária paga aos seus corretores um salário basee de R$1.500,00 .
Além disso, uma comissão de R$200,00 por cada imóvel vendido e 5% do valor de cada venda.
Construa um programa que solicite o nome do corretor, a quantidade de imóveis vendidos e o valor total de suas vendas.
Ao fim, o programa deve calcular e escrever o salário final do corretor de imóveis'''

salario = 1500
comissao = 200

corretor = input("Digite o seu nome: ")
print(corretor)
quantidade_vendas = int(input("Digite a quantidade de imóveis vendidos: "))
print(quantidade_vendas)
valorTotalVendas = float(input("Digite o valor total das suas vendas: "))
print(valorTotalVendas)

comissaoTotal = comissao * quantidade_vendas
bonus = valorTotalVendas * 0.05

print("Comissão total: ", comissaoTotal)
print("Bônus de 5% das vendas: ", bonus)

salarioFinal = salario + comissaoTotal + bonus

print(f"Salario Final do corretor {corretor} é de R$: {salarioFinal:.2f}")

#print("O seu salário total com as comissões e bônus de 5% é: ", salarioFinal)
