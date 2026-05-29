'''Crie um menu:

1 - Adicionar estoque
2 - Retirar estoque
3 - Mostrar estoque
4 - Sair

O produto começa assim:

produto = {
    "nome": "Teclado",
    "estoque": 10
}
Regras
Função adicionar_estoque()
pedir quantidade
adicionar ao estoque
Função retirar_estoque()
pedir quantidade
diminuir estoque

Se tentar retirar mais do que existe:

Estoque insuficiente!
Tratamento de erro

Se digitar texto:

Digite apenas números!

Use:

função
while True
try/except
dicionário'''

def adicionar_estoque(estoque):
    try:
        
        quantidade = int(input("Digite a quantidade a ser adicionada: "))
        
        if quantidade <= 0:
            print("Digite um número maior que zero.")
            return estoque
        
        estoque = estoque + quantidade
        
        print(f"Novo estoque: {estoque}")
        
        return estoque
            
    except ValueError:
        print("Digite apenas números inteiros.")
        
        return estoque


def retirada_estoque(estoque):
    try:
        #print(f"Estoque atual: ")
        quantidade = int(input("Digite a quantia a ser retirada: "))
        
        if quantidade <= 0:
            print("Digite um número maior que zero.")
            return estoque

        if quantidade > estoque:
            print("Quantidade maior que o estoque, tente outra quantia.")
        else:
            estoque = estoque - quantidade
            
        print(f"Novo estoque: {estoque}")    
            
        return estoque
        
    except ValueError:
        print("Digite apenas números inteiros.")
        
        return estoque
        
def mostrar_estoque(estoque):
    print(f"Estoque atual: {estoque}")
    
def menu():
    estoque = 10
    
    while True:
        try:
            print("=====Menu=====")
            print("1 - Adicionar Estoque")
            print("2 - Retirar Estoque")
            print("3 - Mostrar Estoque")
            print("4 - Sair")
            
            opcao = int(input("Digite a opção correspondente: "))
            
            if opcao == 1:
                estoque = adicionar_estoque(estoque)
            elif opcao == 2:
                estoque = retirada_estoque(estoque)
            elif opcao == 3:
                mostrar_estoque(estoque)
            elif opcao == 4:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida, tente novamente.") 
               
        except ValueError:
            print("Digite apenas o número da opção.") 
            
            
menu()                       
        
                    
    