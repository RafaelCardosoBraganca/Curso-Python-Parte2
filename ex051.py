print('{:=^40}','PA DE 10 TERMOS')
n = int(input('Escreve o primeiro termo da PA: '))
r = int(input('Escreva sua razão: '))
dec = (n + (10 - 1)*r) + r

for c in range (n, dec, r):
    print(' {}'.format(c), end=' ->')
print(' ACABOU')