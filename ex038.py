#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

n =int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))

if n > n2:
    print('{} é maior que {}'.format(n, n2))
elif n2 > n:
    print('{} é maior que {}'.format(n2, n))
else:
    print('{} e {} são iguais!'.format(n, n2))
    