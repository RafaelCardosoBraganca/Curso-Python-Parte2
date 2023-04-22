#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: 
#a média de idade do grupo;
#qual é o nome do homem mais velho;
#quantas mulheres têm menos de 20 anos.

soma = 0
older = 0
oldersName = ''
countF = 0

for c in range(1, 5):
    print('------{}ª PESSOA ------'.format(c))
    nome = str(input('NOME: ')).strip().upper()
    idade = int(input('IDADE:  '))
    soma += idade
    sexo = str(input('SEXO - M ou F: ')).strip().lower()
    media = soma / 4
    if sexo == 'm' and c == 1:
        older = idade
        oldersName = nome
    if idade > older and sexo == 'm':
            older = idade
            oldersName = nome
    if sexo in 'f' and idade < 20:
         countF += 1
print('A média de idade dos 4 é', media, 'anos')
print('O homem mais velho tem {} anos e se chama {}'.format(older, oldersName))
print('E há {} mulheres com idade menor à 20 anos'.format(countF))
