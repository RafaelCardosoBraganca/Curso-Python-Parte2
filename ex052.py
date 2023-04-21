#escreva um programa que leia um número e informe se é ou não primo

n = int(input('Digite um número: '))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        div += 1
    else:
        print('\033[31m', end='')
    print(' {}'. format(c), end='')
print('\n\033[m')
print('O número {} foi divido {} vezes'.format(n, div))
if div == 2:
    print('O número é primo')
else:
    print('Não é um número primo')