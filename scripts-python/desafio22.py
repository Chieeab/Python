nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome em minusculo é {}'.format(nome.upper()))
print('Seu nome em maiusculo é {}'.format(nome.lower()))
# nomeseparado = nome.split()
# semespaco = ''.join(nomeseparado)
# print('Seu nome possui {} letras'.format(len(semespaco)))
# print('O primeiro nomte tem {} letras'.format(len(nomeseparado[0])))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem  {} letras'.format(nome.find(' ')))