#progessão aritmética só que com while
#mostrando os 10 primeiros termos da progressão 
#usando a estrutura while.
print ('10 PRIMEIROS TERMOS DE UMA PA')
n = int(input('Primeiro termo: '))
r = int(input('Escreva sua razão: '))
c = 1

while c < 11:
    print('{} ->'.format(n), end=' ')
    c += 1
    n += r
print('FIM')    


