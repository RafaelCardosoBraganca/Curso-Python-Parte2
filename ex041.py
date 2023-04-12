#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa 
#que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
nasc = int(input('Qual a data de nascimento do atleta: '))
idade = atual - nasc

if idade > 25:
    print('{} anos. Categoria: MASTER'.format(idade))
elif 25 <= idade > 19:
    print('{} anos. Categoria: SÊNIOR'.format(idade))
elif 19 <= idade > 14:
    print('{} anos. Categoria: JÚNIOR'.format(idade))
elif 14 <= idade > 9:
    print('{} anos. Categoria: INFANTIL'.format(idade))
elif idade < 9:
    print('{} anos. Categoria: MIRIM'.format(idade))
