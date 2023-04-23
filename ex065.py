'''Exercício Python 65: Crie um programa que leia
 vários números inteiros pelo teclado. 
 No final da execução, mostre a média entre todos 
 os valores e qual foi o maior e o menor valores lidos. 
 O programa deve perguntar ao usuário se ele quer ou não continuar
 a digitar valores.'''
n = c = media = maior = menor =  soma = 0
continuar = ' '

while continuar not in 'NnAaÃãOo':
    n = int(input('Escreva um número: '))
    continuar= str(input('Deseja continuar? Sim ou Não ')).strip()
    c += 1
    soma += n
    if c == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        elif n < menor:
            menor = n
media = soma / c    
print('Você inseriu {} números. O somatório foi {} e a média foi {}'.format(c, soma, media))    
print('O menor foi {} e o maior foi {}'.format(menor, maior))