distancia = int(input('Digite a distancia da sua viagem em Km: '))
if (distancia <= 200):
    print('Para sua viagem de {} Km foi cobrado do valor de R$0,50 por Km totalizando R${}'.format(distancia,distancia*0.50))
else:
    print('Para sua viagem de {} Km foi cobrado do valor de R$0,45 por Km totalizando R${}'.format(distancia,distancia*0.45))