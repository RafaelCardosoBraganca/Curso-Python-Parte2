#faça um scrit que leia um número e mostre seu resultado fatorial

#easy way
from math import factorial
n = int(input('Escreva um número: '))
print('Seu fatorial é: {}'.format(factorial(n)))

#tradicional way
n2 = int(input('Escreva um número, novamente: '))
c = n2
f = 1
print('{}! = '.format(n2), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'. format(f)) 
