from random import randint
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''
0 para PEDRA;
1 Para PAPEL;
2 Para Tesoura;
''')
jogador = int(input('informe a opção:'))
print('o computador ecolheu a opção : {}'.format(opcoes[computador]))
print('o jogador ecolheu a opção:{}'.format(opcoes[jogador]))
if computador == 0 :
    if jogador == 0 :
        print('EMPATE!')
    elif jogador == 1:
        print('VOCE GANHOU!')
    elif jogador == 2:
        print('VOCE PERDEU!')
    else:
        print('Opção incorreta! seu Jamas!')
elif computador == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCE GANHOU!')
    elif jogador == 0:
        print('VOCE PERDEU!')   
elif computador == 2:
    if jogador == 2: 
        print('EMPATE!')
    elif jogador == 0:
        print('VOCE GANHOU!')
    elif jogador == 1:
        print('VOCE PERDEU!')
 
       
