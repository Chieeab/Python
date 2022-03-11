from traceback import StackSummary


salaraio = float(input('Informe seu salario: '))
if(salaraio > 1250.00):
    print('Seu novo salario será de: R${}'.format(salaraio+(salaraio*0.10)))
else:
    print('Seu novo salario será de R${}'.format(salaraio+(salaraio*0.15)))