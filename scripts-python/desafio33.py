n1 = int(input('Informe um numero: '))
n2 = int(input('Informe outro numero: '))
n3 = int(input('Informe mais um numero: '))
if (n1 > n2 and n1 >n3):
    if(n2>n3):
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
elif (n2>n3):
    if(n3>n1):
        print(n2,n3,n1)
    else:
        print(n2,n1,n3)
else:
    if(n1>n2):
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)

