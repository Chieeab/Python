frase = str(input('Digite uma frase: ')).upper()
contagem = frase.count('A')
primeiro = frase.find('A') + 1
ultimo = frase.rfind('A') + 1
print('A letra A aparece {} vezes'.format(contagem))
print('A primeira letra A aparece na posição {}'.format(primeiro))
print('A ultima letra A aparece na posição {}'.format(ultimo))