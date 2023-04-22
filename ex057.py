#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
#mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 0
while sexo != 'f' != 'm':
    sexo = str(input('Digite seu sexo: ')).lower().strip()
    if sexo != 'f' != 'm':
        print('Valor inválido! Tente novamente')
    else:
        print('FIM')



