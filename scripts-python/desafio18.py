import math
angulo = float(input('Digite um angulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('Seno {:.2f}\nCosseno {:.2f}\nTangente{:.2f}'.format(sen,cos,tan))