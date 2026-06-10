'''Exercício 1 - Sistema de Locadora de Filmes

Crie um sistema para registrar locações de filmes.

Tipos de locação
("LANÇAMENTO", "CATALOGO", "PROMOCAO")
Valores
LANÇAMENTO = R$ 20
CATALOGO = R$ 10
PROMOCAO = R$ 5
Dados cadastrados
Nome do cliente
Idade
Tipo de locação
Forma de pagamento (Dinheiro, Pix, Cartão)
Valor da locação
Relatório

Exibir:

Total de locações
Quantidade de lançamentos
Quantidade de catálogo
Quantidade de promoções
Valor total arrecadado
Cliente que gastou mais
Valor gasto pelo cliente

Classificação:

= 500 → Movimento Alto

= 250 → Movimento Médio

Caso contrário → Movimento Baixo

Exibir todos os cadastros.

Salvar relatório em TXT.'''


tipo_locacao = {
    "Lançamento": 20,
    "Catalogo": 10,
    "Promoção": 5
}
locacoes = []

def locacao():
    while True:
        try:
            cliente = {
                "nome": input("Digite o nome do cliente: "),
                "idade": int(input("Digite a idade: "))
            }
            
            for tipo in tipo_locacao:
                print("-", tipo)
                
        except ValueError:
            print("Digite apenas número.")
            
       
        
    
    
    

def menu():
    while True:
        print("Sistema de locação")
        print("1. Registrar locação")
        print("2. Relatório")
        print("3. Sair")
        try:
            opcao = int(input("Digite a opção correspondente: "))
            
            if opcao == 1:
                locacao()
                
            elif opcao == 2:
                print("relatorio")
                
            elif opcao == 3:
                print("Saindo...")
                break
            
            else:
                print("Opção inválida, tente novamente.")
                
        except ValueError:
            print("Digite apenas número.")
            
            
            
menu()            