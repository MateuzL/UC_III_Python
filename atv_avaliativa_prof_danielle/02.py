# Estrutura Condicional: Solicite a nota de um aluno e informe se está aprovado, recuperação ou reprovado.

#Solicitando nota 
nota = float(input("Digite sua nota de 0 a 10: "))

#Estrutura Condicional
if nota < 0 or nota > 10:
    print("Nota inválida.")    #Imprimindo resultado
elif nota >= 0 and nota < 5:
    print("REPROVADO !")
elif nota >= 5 and nota < 7:
    print("RECUPERAÇÃO !")
else:
    print("APROVADO!!!")
    
    