def somatoria (*argumentos):
    soma = 0
    for  i in argumentos:
        soma += i
    return soma

print(somatoria(1, 2, 3, 4, 5))