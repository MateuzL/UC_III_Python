'''def x (y,z):
    res = y + z
    print(res)
#print(x(2))

num = int(input("Valor: "))
num1 = int(input("Valor: "))  
print(x(num,num1))'''


def media(n1, n2, n3, n4):                    #BLOCO DE FUNÇÃO PARA CALCULAR A MÉDIA
    return (n1 + n2 + n3 + n4) / 4

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
print(media(n1, n2, n3, n4))