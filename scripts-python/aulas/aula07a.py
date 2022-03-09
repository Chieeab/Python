from tkinter import E


n1 = int(input('Informe um numero: '))
n2 = int(input('Informe um numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a divisão e {:.2f}'.format(s,m,d), end='')
print('Divisão inteira{},\n e potencia{}'.format(di, e))