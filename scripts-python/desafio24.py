cidade = str(input('Digite o nome de uma cidade: '))
separado = cidade.split()
santo = 'santo' in separado[0].lower()
if (santo == True):
    print ('Possui')
else:
    print('Nao possui')