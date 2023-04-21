#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print("""Suas opções:
0 - PEDRA
1 - PAPEL
2 - TESOURA""")
jogador = int(input('Qual a sua jogada? '))
if jogador > 2:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
elif jogador < 0:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
else:
    computador = randint(0, 2)
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    sleep(1)
    print('JO')
    sleep(1/2)
    print('KEN')
    sleep(1/2)
    print('PO!!!')
    sleep(1)
    print('-=-'*20)


    print('O computador escolheu {} \nO jogador escolheu {}'.format(lista[computador], lista[jogador]))
    print('-=-'*20)

    if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
        print('O JOGADOR VENCEU!') 
    elif jogador == computador:
        print('EMPATE!')
    else:
        print('COMPUTADOR VENCEU!')


