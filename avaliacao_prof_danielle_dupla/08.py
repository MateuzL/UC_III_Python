# Funções: Crie uma função calcular_media() que receba duas notas e retorne a média.

#Solicitando as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a seguna nota: "))

#Função para calcular média
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
    
#Chamando a função
resultado = calcular_media(nota1, nota2)    

#Imprimindo o resultado
print(f"A média é: {resultado}")

    
    
