# Estrutura IF, ELSE e ELIFE
nota1 = float(input("Digite a 1° Nota: "))
nota2 = float(input("Digite a 2° Nota: "))
media = (nota1 + nota2) / 2
print("A sua media é: ", media)
if media >= 60:
    print("APROVADO")
elif media >= 30 and media <= 59:
    print("EXAME FINAL")
else:
    print("REPROVADO")
