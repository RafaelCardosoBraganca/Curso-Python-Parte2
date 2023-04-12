#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, 
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar 
#ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nasc = int(input('Insira seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nasc
if idade < 18 and idade > 0:
    falta = 18 - idade
    print('Você é menor de 18 anos! Ainda faltam {} anos para o seu alistamento'.format(falta))
elif idade == 18:
    print('Já tá na hora de se alistar, meu parceiro, você tem {} anos!'.format(idade))
elif idade > 18:
    passou = idade - 18
    print('Caraca! Tu já passou do ponto, meu compadre. Tu se atrasou só {} anos no seu alistamento kkkkk'. format(passou))
else:
    print('Tu nem nasceu, comédia.')

