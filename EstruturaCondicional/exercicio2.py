#ARVORE DE DECISAO
print("## PROGRAMA DE EMPRESTIMO ##\n")
print("Responda: 0 - NÃO e 1 - SIM\n")

negativado = int(input("Você possui nome NEGATIVADO? "))

if negativado == 1:
    print("Não pode realizar empréstimo.")
else:
    clt = int(input("Possui carteira assinada ?"))
    if clt == 0:
       print("Não pode realizar empréstimo.")
    else:
        casa = int(input("Possui casa própria ?"))
        if casa == 0:
           print("Não pode realizar empréstimo.")
        else:
           print("Conceder Empréstimo")