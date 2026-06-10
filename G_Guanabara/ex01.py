nome = str(input("Digite o nome: ")).title().strip()

primeiro = nome.split()
print(f"Seu primeiro nome é: {primeiro[0]}")
print(f"Seu último nome é: {primeiro[-1]}")
    
