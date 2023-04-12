print('Analisando triângulos: ')
l1 = float(input('Insira o comprimento do lado 1: '))
l2 = float(input('Insira o comprimento do lado 2: '))
l3 = float(input('Insira o comprimento do lado 3: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l2 > l3:
    print('Os seguimentos acima PODEM formar um triângulo do tipo', end=' ')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('ISÓCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os seguimentos acima NÃO PODEM forma um triângulo!')

