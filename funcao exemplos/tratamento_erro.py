try: #Tente executar esse código
    numero = int(input("Digite um número: "))
    
    print(numero)
    
except ValueError:   #Execute esse código
    print("Erro! Por favor, digite apenas números.")
    
finally: #faz mais sentido para banco de dados, fim do bloco
    print("Vou sempre executar!")
    #Utilizado apenas para o usuário.