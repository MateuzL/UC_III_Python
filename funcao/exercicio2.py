"""CONTROLE DE HOTEL
Cadastro de Hóspedes -> Nome, Idade, CPF, Tipo de Quarto, Quantidade de Diárias.                 Quarto/Valor
Reserva de quartos.                                                                           Standard - R$120,00
Quantidade de Diárias.                                                                        Luxo - R$250,00
Valor da Hospedagem.                                                                          Premium - R$400,00
Disponibilidade de quartos.

Situação: Até R$500,00 -> Econômico
          De R$501,00 até R$1500,00 -> Intermediário
          Acima de R$1500,00 -> Premium"""

hospedes = []

def cadastrar_hospede():
    hospede = {}
    try:
        hospede["nome"] = input("Digite o nome do hóspede: ")
        try:
            hospede["idade"] = int(input("Digite a idade do hóspede: "))
        except:
            print("Erro! Idade deve ser um valor numérico. Tente novamente!")
            return
        hospede["cpf"] = input("Digite o CPF do hóspede: ")
        print("Tipos de quarto: Standard R$120,00 - Luxo R$250,00 - Premium R$400,00")
        hospede["tipo_quarto"] = int(input("Digite o tipo de quarto (1 - Standard, 2 - Luxo, 3 - Premium): "))
        hospede["quantidade_diarias"] = int(input("Digite a quantidade de diárias: "))
        
        if hospede["tipo_quarto"] == 1:
            valor_diaria = 120
        elif hospede["tipo_quarto"] == 2:
            valor_diaria = 250
        elif hospede["tipo_quarto"] == 3:
            valor_diaria = 400
        else:
            print("Opção de quarto inválida. Tente novamente!")
            return
        
        valor_hospedagem = valor_diaria * hospede["quantidade_diarias"]
        
        if valor_hospedagem <= 500:
            situacao = "Econômico"
        elif valor_hospedagem <= 1500:
            situacao = "Intermediário"
        else:
            situacao = "Premium"
        
        hospede["valor_hospedagem"] = valor_hospedagem
        hospede["situacao"] = situacao
        
        print("Hóspede cadastrado com sucesso!")
        
        hospedes.append(hospede)
    except:
        print("Erro! Idade e quantidade de diárias devem ser valores numéricos. Tente novamente!")
        
    return hospede

def menu():
    while True:
        print("===MENU===")
        print("1 - Cadastrar Hóspede")
        print("2 - Sair")
        op = int(input("Digite a opção desejada: "))
        
        if op == 1:
            cadastrar_hospede()
            
        elif op == 2:
            print("Saindo do sistema...")
            break

menu()
