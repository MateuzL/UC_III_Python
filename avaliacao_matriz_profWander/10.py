''' Uma escola deseja armazenar as notas de 3 alunos em 4 bimestres.
Utilize uma matriz para armazenar as notas e exiba:
- Todas as notas
- Média de cada aluno
- Situação (Aprovado ou Reprovado)
- Considere média mínima 7'''


notas = []
media = 0


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
    soma = 0
    print(f"Aluno {aluno+1}: ")
    for bimestre in range(len(notas[aluno])):
        soma = soma + notas[aluno][bimestre]     #Somando as notas de cada aluno 
        print(notas[aluno][bimestre], end=" ")
    print()
    media = (soma / len(notas[aluno]))          #Dividindo as notas por 4 para armazenar a média
    print(f"Média: {media}")
    
    #Mostrando a situação de acordo com a média
    if media >= 7:
        situacao = "APROVADO!"
    else:
        situacao = "REPROVADO!"
        
    print(f"Situação: {situacao}")
    print()
    

    
    
