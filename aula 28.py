casa = float(input('digite o valor da casa:'))
salário = float(input('digite a renda:'))
anos = int(input('digite em quantos anos vai pagar:'))
valormensal = casa / anos 
print('valor mensal é de ',round(valormensal))
if valormensal>salário:
    print('não pode pagar')
else:
    print('está permitido pagar')

