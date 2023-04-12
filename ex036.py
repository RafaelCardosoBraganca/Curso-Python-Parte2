#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Insira seu salário: R$ '))
anos = int(input('Em quantos anos deseja pagar?: '))
prestacao = valorCasa / (anos * 12) #valor da prestação
a = salario * 0.3 #variável que corresponde a 30% do salário

print(anos*12)
if prestacao > a:
    print('Infelizmente você é pobre, não podemos ajudar-te :)')
else:
    print('Parabéns! Seu empréstimo foi apravado! O valor mensal da prestação será R${:.2f}'.format(prestacao))


