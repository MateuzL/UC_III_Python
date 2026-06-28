# =========================
# SISTEMA DE HOTEL
# =========================

# Tupla com os tipos de quartos
tipos_quartos = ("standard", "luxo", "premium")

# Dicionário com valores das diárias
valores_quartos = {
    "standard": 120,
    "luxo": 250,
    "premium": 400
}

# Dicionário de disponibilidade
# True = disponível
# False = ocupado
quartos_disponiveis = {
    "standard": True,
    "luxo": True,
    "premium": True
}

# Lista para armazenar hóspedes
hospedes = []


# =========================
# FUNÇÃO CADASTRAR HÓSPEDE
# =========================

def cadastrar_hospede():
    
    print("\n===== CADASTRO DE HÓSPEDE =====")

    nome = input("Digite o nome do hóspede: ")

    # Tratamento de erro
    while True:
        try:
            idade = int(input("Digite a idade: "))

            if idade <= 0:
                print("Digite uma idade válida.")
            else:
                break

        except ValueError:
            print("Erro! Digite apenas números.")

    cpf = input("Digite o CPF: ")

    # Mostrar quartos disponíveis
    print("\n===== QUARTOS DISPONÍVEIS =====")

    for quarto, disponivel in quartos_disponiveis.items():

        if disponivel:
            print(f"{quarto.capitalize()} - DISPONÍVEL")
        else:
            print(f"{quarto.capitalize()} - OCUPADO")

    # Escolha do quarto
    while True:

        tipo_quarto = input(
            "\nEscolha o quarto (standard/luxo/premium): "
        ).lower()

        if tipo_quarto not in tipos_quartos:
            print("Tipo de quarto inválido.")

        elif quartos_disponiveis[tipo_quarto] == False:
            print("Quarto indisponível. Escolha outro.")

        else:
            break

    # Quantidade de diárias
    while True:
        try:
            diarias = int(input("Quantidade de diárias: "))

            if diarias <= 0:
                print("Digite uma quantidade válida.")
            else:
                break

        except ValueError:
            print("Erro! Digite apenas números.")

    # Cálculo do valor total
    valor_total = valores_quartos[tipo_quarto] * diarias

    # Classificação da hospedagem
    if valor_total <= 500:
        categoria = "Econômico"

    elif valor_total <= 1500:
        categoria = "Intermediário"

    else:
        categoria = "Premium"

    # Dicionário do hóspede
    hospede = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "quarto": tipo_quarto,
        "diarias": diarias,
        "valor_total": valor_total,
        "categoria": categoria
    }

    # Adicionar na lista
    hospedes.append(hospede)

    # Reservar quarto
    quartos_disponiveis[tipo_quarto] = False

    print("\nReserva realizada com sucesso!")


# =========================
# FUNÇÃO LISTAR HÓSPEDES
# =========================

def listar_hospedes():

    print("\n===== LISTA DE HÓSPEDES =====")

    if len(hospedes) == 0:
        print("Nenhum hóspede cadastrado.")
        return

    for hospede in hospedes:

        print(f"""
Nome: {hospede["nome"]}
Idade: {hospede["idade"]}
CPF: {hospede["cpf"]}
Quarto: {hospede["quarto"]}
Diárias: {hospede["diarias"]}
Valor Total: R$ {hospede["valor_total"]:.2f}
Categoria: {hospede["categoria"]}
""")


# =========================
# FUNÇÃO MOSTRAR QUARTOS
# =========================

def mostrar_quartos():

    print("\n===== SITUAÇÃO DOS QUARTOS =====")

    for quarto, disponivel in quartos_disponiveis.items():

        if disponivel:
            print(f"{quarto.capitalize()} - DISPONÍVEL")

        else:
            print(f"{quarto.capitalize()} - OCUPADO")


# =========================
# MENU PRINCIPAL
# =========================

while True:

    print("""
========== HOTEL ==========

1 - Cadastrar hóspede
2 - Listar hóspedes
3 - Mostrar quartos disponíveis
4 - Sair
""")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_hospede()

        elif opcao == 2:
            listar_hospedes()

        elif opcao == 3:
            mostrar_quartos()

        elif opcao == 4:
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")

    except ValueError:
        print("Erro! Digite apenas números.")