"""Construa um programa que solicite ao usuário dois números positivos.
Em seguida, o programa deve presentar o seguinte menu:
1. Média ponderada, com pesos 2 e 3, respectivmente
2. Quadrado da soma dos 2 números
3. Cubo do menor número
Escolha uma opção:
De acordo com a opçao informada, o programa deve calcular a operação apresentada no menu.
Se a opção esolhida for inválida, o programa deve mostrar a mensagem "Opção inválida" e ser encerrado.
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha uma opção")
print("1. Média ponderada, com pesos 2 e 3, respectivmente")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número")

opção = int(input("Digite o número da sua opção: "))

if opção < 1 or opção > 3:
    print("OPÇAO INVÁLIDA!!!")
    exit()

elif opção == 1:
    media1 = num1 * 2
    media2 = num2 * 3
    somaponderada = (media1 + media2) / 5
    # OU assim: media = (num1 *2) + (num2 *3) / 5
    print(f"Média ponderada: {somaponderada:.2f}")

elif opção == 2:
    quadradosoma = (num1 + num2) ** 2
    print(f"O quadrado da soma dos números é {quadradosoma}")

elif opção == 3:
    if num1 < num2:
        cubonum1 = num1**3
        print(f"O cubo do menor número é {cubonum1}")
    elif num2 < num1:
        cubonum2 = num2**3
        print(f"O cubo do menor número é {cubonum2}")    
