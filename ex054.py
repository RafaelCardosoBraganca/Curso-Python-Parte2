#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maioridade = 0
menoridade = 0
for c in range(1, 8):
    anoNasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year  - anoNasc
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('A quantidade de maiores de idade é igual à {}, e a quantidade de menores de idade é igual à {}'.format(maioridade, menoridade))
