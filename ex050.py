#Exercício Python 50: Desenvolva um programa que leia seis números inteiros 
#e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
s = 0
count = 0
for c in range(0,6):
    n = int(input('Escreva um número: '))
    if n % 2 == 0:
        s += n
        count += 1
print('Você informou {} números pares e soma deles é = {}'.format(count, s))

