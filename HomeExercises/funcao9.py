'''Crie duas funções:

adicionar_estoque()
retirar_estoque()

O sistema deve:

começar com estoque = 10
permitir adicionar
permitir retirar
impedir estoque negativo'''

def adicionar_estoque(estoque):
    print(f"Estoque atual: {estoque}")
    quantidade = int(input("Digite a quantidade a adicionar no estoque: "))
    estoque = estoque + quantidade
    return estoque
    
    
 
def retirar_estoque(estoque):
    print(f"Estoque atual: {estoque}")
    quantidade = int(input("Digite a quantidade a retirar do estoque: "))
    if quantidade > estoque:
        print("Quantidade maior que o estoque existente, tente outra quantia.")
    else:
        estoque = estoque - quantidade
        
    return estoque    
    
    
def menu():
    estoque = 10
    while True:
        print("===Menu====")
        print(f"Estoque atual: {estoque}")
        print("1 - Adicionar estoque")
        print("2 - Retirar estoque")
        print("3 - Sair")
        
        opcao = int(input("Digite a opção: "))
        
        if opcao == 1:
            estoque = adicionar_estoque(estoque)
        elif opcao == 2:
            estoque = retirar_estoque(estoque)
        elif opcao == 3:
            print("Saindo do Sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")
            
menu()                
        
