# Dicionários: Cadastre nome, idade e curso utilizando um dicionário e exiba as informações.


#Cadastrando os dados no dicionario
dicionario = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: ")),
    "curso": input("Digite seu curso: ")
}

#Exibindo os dados solicitados
print(f"Nome: {dicionario['nome']}")
print(f"Idade: {dicionario['idade']}")
print(f"Curso: {dicionario['curso']}")
