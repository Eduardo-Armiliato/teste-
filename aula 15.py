from math import hypot

co = float(input('informe o cateto oposto: '))
ca = float(input('informe o catero adjacente: '))
# hi = (co ** 2 + ca **2) ** (1/2)

# print('formula matematica) A hipotenusa:{:.2f}'.format(hi))
hi = hypot(co, ca)
print('(formula matematica)A Hipotenusa: {:.2f}' .format(hi))
