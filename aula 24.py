n1 = int(input('Digite um ano:'))


if (n1%4==0 and n1%100!=0) or (n1%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')


