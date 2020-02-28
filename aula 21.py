from random import randint
computador = randint(0, 5) #faz o computador "PENSAR"
print('-=-' * 20)
print('vou pensar em um numero tente adivinhar ...')
print('-=-' * 20)
jogador = int(input('em que numero pensei?'))#jogador tenta adivinhar 
if jogador == computador:
    print('parabéns você conseguiu ganhar de um computador')
else:
    print('mee perdeu seu merdinha')

