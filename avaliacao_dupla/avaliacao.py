'''Crie um sistema para Clínica médica registrar seus pacientes, tipos de atendimento, valor do atendimento.

O sistema deve ao final emitir relatorio com o total de atendimento, quantidade de exames, consultas, retornos e o valor total arrecadado.
Também deve imprimir o valor do atendimento mais alto junto com o nome do paciente.
imprimir no relatorio todos os cadastros, com nome do paciente, idade, tipo de atendimento, forma de pagamento e valor cobrado.
Se o valor total arrecadado for maior ou igual a 1000, deverá exibir "movimento alto", se for maior ou igual a 500 e menor que 1000, deverá exibir
"movimento médio". Caso contrário, deverá exibir "movimento baixo".
salvar em arquivo txt.'''

tipos_atendimento = ("CONSULTA", "EXAME", "RETORNO")

forma_pagamento = ("Dinheiro", "Pix", "Cartao")

usuarios = []

def cadastrar_atendimento():
    while True:

        usuario = {}
        
        print("Tipos de atendimento:")
        
        for tipos in tipos_atendimento:
            
            print("-", tipos)

        usuario["tipo_atendimento"] = input("Digite o tipo de problema: ").upper()

        if usuario["tipo_atendimento"] == "CONSULTA":
            usuario["valor"] = 200
            print("Valor R$200,00")

        elif usuario["tipo_atendimento"] == "EXAME":
            usuario["valor"] = 100
            print("Valor R$100,00")

        elif usuario["tipo_atendimento"] == "RETORNO":
            usuario["valor"] = 50
            print("Valor R$ 50,00")

        if usuario["tipo_atendimento"] not in tipos_atendimento:
            print("Tipo de atendimento inválido.")
            return
        
        usuario["nome"] = input("Digite o nome do paciente: ")

        try:
            usuario["idade"] = int(input("Digite a idade do paciente: "))

            print("Formas de pagamento: ")
            for forma in forma_pagamento:
                print("-", forma)

            usuario["forma_pagamento"] = input("Digite a forma de pagamento: ") 

            if usuario["forma_pagamento"] not in forma_pagamento:
                print("Forma de pagamento inválida.")
                return

            usuarios.append(usuario)

            continuar = int(input("Deseja cadastrar outro paciente? (1-SIM/2-NAO)"))
            if continuar == 2:
                break

        except ValueError:
            print("Digite apenas numeros")



def gerar_relatorio():
    arquivo = open("C:/Users/lucen/Documents/avaliacao_clinica.txt", "w", encoding="utf-8")

    arquivo.write()


    print("Arquivo salvo com sucesso!")
    print("=====RELATÓRIO DA CLÍNICA===== ")

    
    if len(usuarios) == 0:
        print("Nenhum atendimento cadastrado.")
        return
    

    total_atendimentos = len(usuarios)
    qtd_consultas = 0
    qtd_exames = 0
    qtd_retorno = 0
    valor_total = 0
    maior_valor = 0
    paciente_maior_valor = ""


    for usuario in usuarios:
        valor_total += usuario["valor"]

        if usuario["tipo_atendimento"] == "CONSULTA":
            qtd_consultas += 1

        elif usuario["tipo_atendimento"] == "EXAME":
            qtd_exames += 1

        elif usuario["tipo_atendimento"] == "RETORNO":
            qtd_retorno += 1

        

        if usuario["valor"] > maior_valor:
            maior_valor = usuario["valor"]
            paciente_maior_valor = usuario["nome"]

        if valor_total >= 1000:
            movimento = "Movimento alto"

        elif valor_total >= 500 and valor_total < 1000:
            movimento = "Movimento Médio"

        else:
            movimento = "Movimento baixo"

        print(f"Quantidade Total de Atendimentos: {total_atendimentos}")
        print(f"Quantidade total de Consultas: {qtd_consultas}")
        print(f"Quantidade total de Exames: {qtd_exames}")
        print(f"Quantidade total de Retorno: {qtd_retorno}")
        print(f"Valor total arrecadado: {valor_total:.2f}")
        print(f"Paciente com maior valor: {paciente_maior_valor} Valor gasto: {maior_valor:.2f}")
        print(f"Movimento da clínica: {movimento}")

        print("=" *20)

    for usuario in usuarios:
        print(f"Nome: {usuario["nome"]}")
        print(f"Idade: {usuario["idade"]}")
        print(f"Tipo de Atendimento: {usuario["tipo_atendimento"]}")
        print(f"Forma de Pagamento: {usuario["forma_pagamento"]}")
        print(f"Valor Cobrado: {usuario["valor"]:.2f}")
    
    arquivo.close()


def menu():
    while True:
        print("====MENU====")
        print("1. Cadastrar atendimento")
        print("2. Imprimir Relatorio")
        print("3. Sair")
        try:
            op = int(input("Digite sua opção: "))

            if op == 1:
                cadastrar_atendimento()

            elif op == 2:
                gerar_relatorio()

            elif op == 3:
                print("Saindo...")
                break

            else:
                print("Opção inválida, tente novamente.")

        except ValueError:
            print("Digite apenas números.")


menu()