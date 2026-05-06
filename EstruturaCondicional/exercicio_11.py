"""Uma empresa concederá um aumento de salário aos seus funcionários,
variável de acordo com o cargo, conforme a tabela abaixo:

Cargo aumento                 (%)
Programador de Sistemas       30
Analista de Sistemas          20
Analista de Banco de Dados    15

Crie um programa que solicite ao usuário o salário e o cargo de um determinado funcionário.
Na sequência, o programa deve calcular e imprimir o seu novo salário.
Caso o cargo informado não esteja na tabela, o programa deve imprimir "Cargo inválido"
"""
print("-------------------------------------")
salario = float(input("Digite o seu salário: "))
print(f"Salário: R$ {salario:.2f}")

print("-------------------------------------")
print("Veja os cargos abaixo e digite a sua opção")
print("1. Programador de Sistemas")
print("2. Analista de Sistemas")
print("3. Analista de Banco de Dados")
print("-------------------------------------")


cargo = int(input("Digite a opção (1 A 3): "))
print(f"Cargo selecionado: {cargo}")

if cargo < 1 or cargo > 3:
    print("CARGO INVÁLIDO!")
    exit()
elif cargo == 1:
    novo_salario = salario + salario * 0.30
    print(f"O seu novo salário é R$ {novo_salario}")
elif cargo == 2:
    novo_salario = salario + salario * 0.20
    print(f"O seu novo salário é R$ {novo_salario}")
else:
    novo_salario = salario + salario * 0.15
    print(f"O seu novo salário é R$ {novo_salario}")
