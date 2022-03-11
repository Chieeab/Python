ano = int(input('Infome um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('\033[31;43mÉ um ano bissexto\033[m')
else:
    print('Não é bissexto')