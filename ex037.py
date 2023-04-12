#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer 
#e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número: '))
print("""Selecione uma das três opções para converter seu número
1 - binário
2 - octal
3 - hexadecimal""")
opcao = int(input('Escreva a opção desejada: '))

if opcao == 1:
    print('O número {} convertido para binário, é {}'.format(n, bin(n) [2:]))
elif opcao == 2:
    print('O número {} convertido para octal, é {}'.format(n, oct(n) [2:]))
elif opcao == 3:
    print('O número {} convertido para hexadecial, é {}'.format(n, hex(n) [2:].upper()))
else:
    print('OPÇÃO INVÁLIDA! :(')


