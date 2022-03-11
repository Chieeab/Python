lado1 = int(input('Informe um lado do triangulo: '))
lado2 = int(input('Informe um lado do triangulo: '))
lado3 = int(input('Informe um lado do triangulo: '))

if(lado1< lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 +  lado2):
    print('E possivle formar um triangulo')
else:
    print('Não é possivel formar um triangulo')