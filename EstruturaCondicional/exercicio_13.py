"""ELABORE UM ALGORITMO PARA DIAGNOSTICAR GRIPE COMUM.
USE OS SEGUINTES FATORES:
SINTOMAS -> FEBRE MODERADA, NARIZ ENTUPIDO, DOR DE GARGANTA, TOSSE
DURAÇÃO DOS SINTOMAS -> MENOR QUE 7 DIAS, MAIOR QUE 7 DIAS
CLASSIFICAÇÃO: PROVÁVEL GRIPE COMUM OU SINTOMAS ATÍPICOS, INVESTIGAR OUTRAS CONDIÇÕES"""

print("Vamos diagnosticar sua gripe:")

duração_sintoma = int(input("Você tem sintomas a mais de 7 dias?  1 - SIM OU 0 - NAO"))
print(duração_sintoma)

if duração_sintoma == 0:
    print("Você não está com gripe!")
    exit()

febre = int(input("Você tem febre?  1 - SIM OU 0 - NAO"))

nariz_entupido = int(input("Você está com o nariz entupido?  1 - SIM OU 0 - NAO"))

dor_garganta = int(input("Você está com dor de garganta?  1 - SIM OU 0 - NAO"))

tosse = int(input("Você está com tosse?  1 - SIM OU 0 - NAO"))

if febre + nariz_entupido + dor_garganta + tosse == 4:
    print("Você está gripado!")
else:
    febre + nariz_entupido + dor_garganta + tosse <= 3
    print("Provável sintoma de gripe, investigar outras condições.")
