# Exercicio para desenvolver um programa que calcule o preço.

print("Cada camisa é R$12.50")
print("Até 5 camisas, desconto de 3%")
print("Acima de 5 camisas e até 10 camisas, desconto de 5%")
print("Acima de 10 camisas, descontos de 7%")
numeroCamisa = int(input("Digite a quantidade de camisas que você deseja: "))
valorCamisa = 12.50
valorFinal = numeroCamisa * valorCamisa

if numeroCamisa <= 5:
    #valorFinal = valorFinal * (1 - 3 / 100)
    valorDesconto = valorFinal * 0.03
    totalFinal = valorFinal - valorDesconto

elif numeroCamisa > 5 and numeroCamisa <= 10:
    #valorFinal = valorFinal * (1 - 5 / 100)
    valorDesconto = valorFinal * 0.05
    totalFinal = valorFinal - valorDesconto
else:
    numeroCamisa > 10
#valorFinal = valorFinal * (1 - 7 / 100)
    valorDesconto = valorFinal * 0.07
    totalFinal = valorFinal - valorDesconto
    
print(f"Valor total com desconto R$ {totalFinal:.2f}")
