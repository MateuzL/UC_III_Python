'''Crie uma função chamada dividir() que:

peça dois números
faça a divisão
Regras
Se dividir por zero:

Mostrar:

Não é possível dividir por zero!
Se digitar texto:

Mostrar:

Digite apenas números!'''


def dividir():
    while True:
        try:
            a = float(input("Digite o primeiro numero: "))
            b = float(input("Digite o segundo numero: "))
            
            resultado = a / b
            
            print(f"A divisão de {a} por {b} é: {resultado}")
            
            break
        
        except ZeroDivisionError:
            print("Não é possível dividir por 0")
            
        except ValueError:
            print("Digite apenas Números.")
            
    
    
dividir()        