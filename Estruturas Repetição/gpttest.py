pessoa = []

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input("Digite sua cidade: ")
    
    dados = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }
    
    pessoa.append(dados)
    
    continuar = int(input("Deseja cadastrar mais? 1 - SIM / 2 - NAO"))
    if continuar == 2:
        break
    
print("\nLista de Pessoas: \n")    
for dados in pessoa:
    print(f"\nNome: {dados['nome']}")
    print(f"Idade: {dados['idade']}")
    print(f"Cidade: {dados['cidade']}")
        
