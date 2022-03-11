nome = str(input('Digite seu nome completo: '))
nome_separado = nome.split()
print(len(nome_separado))
print('Seu primeiro nome é {} e seu ultimo nome é {}'.format(nome_separado[0],nome_separado[len(nome_separado)-1]))