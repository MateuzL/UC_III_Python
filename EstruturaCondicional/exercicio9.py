print("Operação de Divisão")

while True:
    n1 = int(input("Informe o 1° Numero: "))
    n2 = int(input("Informe o 2° Numero: "))
    
    if n2 == 0:
        print("Divisor não pode ser por 0")
        break
    
    print(f"{n1} / {n2} = {(n1/n2):.2f}") 

print("Fim da Operação")   