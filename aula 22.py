velocidade = float(input('velocidade:'))
multa = (velocidade - 80)*7
if (velocidade < 80):  
    print('limpo')
else:
    print('multado, sua multa é de R${}.'.format(multa))
    

