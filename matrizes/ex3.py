notas = []

for i in range(3):
    linha = []
    for j in range(3):
        msg = f'Nota {j+1} do aluno {i+1}: '
        linha.append(float(input(msg)))
        
    notas.append(linha)
    
    
print(notas)