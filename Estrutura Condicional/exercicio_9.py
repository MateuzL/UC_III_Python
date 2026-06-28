'''Construa um programa que receba um número inteiro positivo informado pelo usuário.
Caso ele seja par, o programa deve calcular o seu quadrado.
Mas se ele for ímpar, deve ser calculado o seu cubo.
Ao fim, o programa deve imprimir o valor calculado.'''

x = int(input("Informe um número: "))
if x % 2 == 0:
    xquadrado = x**2
    print(f"O seu número {x} em quadrado é: {xquadrado}")
else:
    xcubo = x**3
    print(f"O seu número {x} ao cubo é: {xcubo}")
    
     
