'''Uma transportadora deseja calcular prioridade de entrega.
Receba os dados; distancia da entrega
urgente? SIM OU NAO 
classificação: 
Urgente -> entrega prioritaria
distancia acima de 300 -> entrega longa
distancia abaixo de 300 -> entrega padrao'''

print("Calcular prioridade de entrega: ")
print("Responda com 1 - SIM OU 0 - NAO")
urgente = int(input("Sua entrega é urgente? 1 - SIM OU 0 - NAO"))
if urgente == 1:
    print("Entrega prioritária!")
    exit()
else:
    urgente == 0
    print("Entrega não prioritária")

distancia = int(input("Digite a distancia da entrega em km: "))
print(f"Distância da entrega: {distancia}")

if distancia > 300:
    print(f"Distancia: {distancia} acima de 300km, entrega longa.")
else:
    distancia < 300
    print(f"Distância: {distancia} menos de 300km, entrega padrão.")        
    


 

