#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('Insiria a nota 1: '))
n2 = float(input('Insiria a nota 2: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Sua média foi {:.1f} -- APROVADO!'.format(media))
elif media < 7 and media >= 5:
    print('Sua média foi {} -- VOCÊ ESTÁ EM RECUPERAÇÃO!'.format(media))
else:
    print('Sua média foi {} -- VOCÊ FOI REPROVADO!'.format(media))

