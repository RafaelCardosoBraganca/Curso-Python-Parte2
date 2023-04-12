#Exercício Python 43: Desenvolva uma lógica que leia
#o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
#de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
print('Calculando seu IMC!')
print('Em KG preciso que me informe...')
p = float(input('Qual seu peso? '))
print('Em METROS me preciso que informe... ')
h = float(input('Qual sua altura? ' ))
imc = p / h ** 2
print('Seu IMC é {:.1f}, você está '.format(imc), end='')

if imc < 18.5:
    print('ABAIXO DO PESO!!')
elif imc < 25:
    print('NO PESO IDEAL!!')
elif imc < 30:
    print('COM SOBREPESO!!')
elif imc < 40:
    print('COM OBESIDADE!!')
else:
    print('COM OBESIDADE MÓRBIDA!!')

