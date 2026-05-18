alunos = []

for i in range(2):
    aluno = {
        "nome": input("Digite nome do aluno: "),
        "idade": int(input("Digite a idade do aluno: "))
    }
    
    alunos.append(aluno)
    
    continuar = int(input("Deseja continuar cadastros? 1 - SIM/ 2 - NAO"))
    if continuar == 2:
        break
   
    