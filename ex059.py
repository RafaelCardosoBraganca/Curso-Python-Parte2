'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input('Escreva um número: '))
n2 = float(input('Escreva outro número '))
choice = 0
maior = 0

while choice != 5:
    print("""[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
    """)
    choice = int(input('Sua opção: '))
    if choice == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif choice == 2:
        print('O produto de {} e {} é {}'.format(n1, n2, n1*n2))
    elif choice == 3:
        if n1 > n2:
            print('Entre {} e {} , {} é maior'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} , {} é maior'.format(n1, n2, n2))
        else:
            print('Os números são iguais')
    elif choice == 4:
        n1 = float(input('Escreva um número: '))
        n2 = float(input('Escreva outro número: '))
    elif choice > 5 or choice < 1:
        print('Opção Inválida')
print('FIM!')       