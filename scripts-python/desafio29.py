velocidade = int(input('Quantos Km/h você está: '))

if (velocidade > 80):
    print('Você foi multado, o valor da multa é de ')
    valor = (velocidade - 80) * 7.00
    print('O valor da multa é de R${:.2f}'.format(valor))
else:
    print('Você não foi multado :)')