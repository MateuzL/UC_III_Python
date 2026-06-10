# Tuplas: Crie uma tupla com os meses do ano e exiba o mês correspondente ao número informado pelo usuário.


#Tupla com os meses
tupla = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

#Solicitando o mês 
print("===Meses do ano===")
mes = int(input("Digite o número do mês (1 a 12) para descobrir qual mês é: "))

#Imprimindo o mês correspondente
print(f"O mês {mes} é: {tupla[mes-1]}")