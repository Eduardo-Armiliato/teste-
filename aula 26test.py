n1 = float(input('digite um valor:'))
if n1 >= 1200:
    n1 = (n1 * 0.10) + n1
else:
    n1 = (n1 * 0.15) + n1
print('O valor de pi formatado é: {:.2f}'.format(n1),'reais')