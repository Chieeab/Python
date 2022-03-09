largura = int(input('Insira a largura da parede em metros: '))
altura = int(input('Insira a altura da parede em metros: '))
area = largura * altura
tinta  = 2
print('É possivel pintar {} m2'.format(area/tinta))
print('Será preciso de {} Litros de tinta'.format(area//tinta))