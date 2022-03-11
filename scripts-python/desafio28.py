import random
sorteio = random.randint(0,5)
numero = int(input('Escolha um numero: '))
if (numero == sorteio):
    print('Você acertou')
else:
    print('Você errou')