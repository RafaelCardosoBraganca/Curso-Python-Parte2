'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para 
o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('10 PRIMEIROS TERMOS DE UMA PA')
first = int(input('Primeiro termo: '))
r = int(input('Razão: '))
term = first
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print('{} ->'.format(term), end=' ')
        c += 1
        term += r
    print('Pausa')
    mais = int(input('Deseja mostrar mais quantos termos? '))
print('Fim da PA, {} termos foram mostrados!'.format(total))




    