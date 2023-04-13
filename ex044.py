#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por uma compra,
#considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
from time import sleep 
print('{:=^40}'.format('Letticia Tapetes')) #piada interna com a minha esposa
print('{:^40}'.format('Seja Bem-Vindo!!'))
preco = float(input('Qual o total da sua compra?: R$ '))
print("""Em qual forma deseja realizar seu pagamento
1 - À vista dinheiro/cheque;
2 - À vista no cartão;
3 - Em até 2x no cartão;
4 - 3x ou mais no cartão.""")
opcao = int(input('Insira o número da opção desejada: '))
print('Carregando...')
sleep(3)
if opcao == 1:
    preco = preco - 0.1 * preco
    print('Você recebeu 10%', 'de desconto! Sua compra sairá por R${:.2f}'.format(preco))
elif opcao == 2:
    preco = preco - 0.05 * preco
    print('Você recebeu 5%', 'de desconto! Sua compra sairá por R${:.2f}'.format(preco))
elif opcao == 3:
    print('Sua compra sairá por R${:.2f} em 2x SEM JUROS. Sendo cada par5cela R${:.2f}'.format(preco, preco / 2))

elif opcao == 4:
    vezes =  int(input('Insira o número de parcelas: '))
    if vezes > 2:
        preco = preco + preco * 0.2
        parcela = preco / vezes
        print("""Você parcelou em {}x. Os juros serão de 20%. 
O Preço total a pagar é de R${:.2f}
e cada parcela saíra por R${:.2f}""".format(vezes, preco, parcela))
    else:
        print('OPÇÃO INVÁLIDA! Somente a partir de 3 parcelas! Tente novamente.')
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE')




