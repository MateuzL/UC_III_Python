'''Implemente um programa que converta o valor de uma velocidade média em km/h para m/s.
Para isso, o usuário deve informar o valor da velocidade média.
Sabe-se que o fator utilizado para essa conversão é 3,6.'''

velmedia = float(input("Digite a velocidade media em km/h: "))
velsegundos = velmedia / 3.6
print(f"{velmedia:.2f} Km/h equivale a {velsegundos:.2f} m/s")

