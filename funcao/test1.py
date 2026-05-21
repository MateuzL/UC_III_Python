# CONTROLE DE HOTEL

hospedes = []
quartos = {
    "Standard": 120,
    "Luxo": 250,
    "Premium": 400
}

disponibilidade = {
    "Standard": 1,
    "Luxo": 1,
    "Premium": 1
}


# FUNÇÃO PARA CLASSIFICAR A HOSPEDAGEM
def classificar(valor_total):
    if valor_total <= 500:
        return "Econômico"
    elif valor_total <= 1500:
        return "Intermediário"
    else:
        return "Premium"


# FUNÇÃO PARA CADASTRAR HÓSPEDE
def cadastrar_hospede():

    print("\n--- CADASTRO DE HÓSPEDE ---")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")

    print("\nTipos de quartos disponíveis:")
    
    for tipo in quartos:
        print(f"{tipo} - R${quartos[tipo]}")

    tipo_quarto = input("\nEscolha o tipo de quarto: ")

    # VERIFICA DISPONIBILIDADE
    if tipo_quarto not in disponibilidade:
        print("Tipo de quarto inválido!")
        return

    if disponibilidade[tipo_quarto] <= 0:
        print("Quarto indisponível!")
        return

    diarias = int(input("Quantidade de diárias: "))

    valor_total = quartos[tipo_quarto] * diarias

    situacao = classificar(valor_total)

    # DIMINUI A DISPONIBILIDADE
    disponibilidade[tipo_quarto] -= 1

    # DICIONÁRIO DO HÓSPEDE
    hospede = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "quarto": tipo_quarto,
        "diarias": diarias,
        "valor_total": valor_total,
        "situacao": situacao
    }

    hospedes.append(hospede)

    print("\nHóspede cadastrado com sucesso!")


# FUNÇÃO PARA MOSTRAR HÓSPEDES
def mostrar_hospedes():

    print("\n--- LISTA DE HÓSPEDES ---")

    if len(hospedes) == 0:
        print("Nenhum hóspede cadastrado.")
        return

    for hospede in hospedes:

        print("\nNome:", hospede["nome"])
        print("Idade:", hospede["idade"])
        print("CPF:", hospede["cpf"])
        print("Quarto:", hospede["quarto"])
        print("Diárias:", hospede["diarias"])
        print("Valor Total: R$", hospede["valor_total"])
        print("Situação:", hospede["situacao"])


# FUNÇÃO PARA MOSTRAR DISPONIBILIDADE
def mostrar_disponibilidade():

    print("\n--- DISPONIBILIDADE DE QUARTOS ---")

    for tipo in disponibilidade:
        print(tipo, ":", disponibilidade[tipo], "quartos disponíveis")


# MENU PRINCIPAL
opcao = ""

while opcao != "4":

    print("\n========== CONTROLE DE HOTEL ==========")
    print("1 - Cadastrar Hóspede")
    print("2 - Mostrar Hóspedes")
    print("3 - Mostrar Disponibilidade")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_hospede()

    elif opcao == "2":
        mostrar_hospedes()

    elif opcao == "3":
        mostrar_disponibilidade()

    elif opcao == "4":
        print("Sistema encerrado.")

    else:
        print("Opção inválida!")