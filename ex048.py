#Exercício Python 48: Faça um programa que calcule a soma entre todos os números ímpares que são 
#múltiplos de três e que se encontram no intervalo de 1 até 500.
import time
print('Mostre-me a soma todos os ímpares e múltiplos de 3!')
time.sleep(1)
print('é pra já, meu nobre!')
time.sleep(1)
print('-=-'*20)
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('O somatório dos {} números solicitados é= {}'.format(cont, s))