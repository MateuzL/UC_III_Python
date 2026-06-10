''' Uma escola deseja armazenar as notas de 3 alunos em 4 bimestres.
Utilize uma matriz para armazenar as notas e exiba:
- Todas as notas
- Média de cada aluno
- Situação (Aprovado ou Reprovado)
- Considere média mínima 7'''


notas = []

#Solicitando notas
for aluno in range(3):
    print(f"Aluno {aluno+1}: ")
    linha = []
    for bimestre in range(4):
        nota = float(input(f"Digite a {bimestre+1}ª Nota: "))
        linha.append(nota)
    notas.append(linha)
    
#Mostrando todas as notas
for aluno in range(len(notas)):
    print(f"Aluno {aluno+1}: ")
    for bimestre in range(len(notas[aluno])):
        print(notas[aluno][bimestre], end=" ")
    print()
    
