'''Exercício Python 64: Crie um programa que leia vários 
números inteiros pelo teclado. O programa só vai parar 
quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual 
foi a soma entre eles (desconsiderando o flag).'''
import time
n = 0
soma = 0
c = 0
while n != 999:
    n =  int(input('Escreva um número: '))
    print('Caso deseje encerrar, digite 999')
    print('-'*40)
    time.sleep(0.3)
    if n != 999:   
        soma += n
        c += 1
print('~'*40)
print('Você inseriu {} números, a soma entre eles é: {}'.format(c, soma))
    