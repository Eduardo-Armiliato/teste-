salario = float(input('digite o o salario do funcionário:'))
salarinc = salario 
print('o salario inicial é de ',salarinc)
if salario >= 1200:
    salario = (salario * 0.10) + salario
else:
    salario = (salario * 0.15) + salario
print('o salario atual é de ',salario)
aumento = salario * 0.1 
print('o aumento é de ', aumento,)


