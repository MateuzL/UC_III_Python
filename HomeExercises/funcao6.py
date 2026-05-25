'''Crie uma função chamada adicionar_notas() que:

peça 3 notas usando for
armazene em uma lista
mostre:
lista completa
média das notas'''
notas = []
def adicionar_notas():
    for i in range(3):
        nota = float(input(f"Digite a {i + 1}ª Nota: "))
        notas.append(nota)
    print("======================")
    print("Notas: ")    
    for nota in notas:
        print(nota)
   
    
        
        
adicionar_notas()
media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f}")    
    

