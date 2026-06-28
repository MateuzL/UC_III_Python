alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):

    nome = input("Nome: ")

    notas = []

    for j in range(4):
        nota = float(input(f"Digite a {j+1}ªNota: "))
        notas.append(nota)

    media = sum(notas) / 4

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media
    }

    alunos.append(aluno)

print("\nLISTA DE ALUNOS")

for aluno in alunos:
    print("----------------")
    print("Nome:", aluno["nome"])
    #print("Notas:", aluno["notas"])
    print("Média:", aluno["media"])