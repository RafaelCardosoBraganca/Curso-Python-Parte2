#faça um script que leia uma frase e diga se é um palíndromo 
frase = str(input('Escreva uma frase: ')).strip().upper()
words = frase.split()
junto = ''.join(words)
inverso = junto[::-1]

print('o inverso de {} é {}'.format(junto, inverso))

if junto == inverso:
    print('é um palíndromo')
else:
    print('não é um palíndromo')
    