# Arquito TXT: Solicite o nome de um aluno e grave a informação em um arquivo alunos.txt


#Solicitando o nome do aluno
aluno = input("Digite seu nome: ")

arquivo = open('C:/Users/vboxuser/Documents/aluno.txt', 'w', encoding='utf-8') #Abrindo arquivo
arquivo.write(f"Aluno: {aluno}")  #Escrevendo no arquivo
arquivo.close()   #Fechando arquivo
