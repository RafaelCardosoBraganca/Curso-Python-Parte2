#Exercício Python 58: Melhore o jogo do DESAFIO 28 
#onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final: 
#quantos palpites foram necessários para vencer.
from random import randint
from time  import sleep
print('O computador pensou em um número entre 0 e 10')
print('Tente advinhar!')
c = randint(0, 10)
guess = int(input('Escreva o número: '))
sleep(1)
times = 0

while guess != c:
    if guess > c:
        print('Menos... Tente novamente!')
    else:
        print('Mais... Tente novamente!')
    guess = int(input('Escreva o número: '))
    sleep(1)
    times += 1
print('Parabéns, você acertou e levou {} tentativas'.format(times))
