numero = int(input('Digite um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
# print('unidade {}'.format(numero[3]))
# print('dezena {}'.format(numero[2]))
# print('centena {}'.format(numero[1]))
# print('milhar {}'.format(numero[0]))
print('unidade {}'.format(unidade))
print('dezena {}'.format(dezena))
print('centena {}'.format(centena))
print('milhar {}'.format(milhar))