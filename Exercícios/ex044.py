# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço 
# normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

print( "{:.^40}".format(" LOJAS RAFAEL "))
preco = float(input("Preço das compras: R$"))

print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")

opcao = int(input("Qual é a opção? "))

if opcao == 1:
    precoFinal = preco - (preco * 10 / 100)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, precoFinal))
elif opcao == 2:
    precoFinal = preco - (preco * 5 / 100)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, precoFinal))
elif opcao == 3:
    parcelas = preco / 2
    precoFinal = preco
    print("Sua compra será parcelada em 2x de R${} SEM JUROS".format(parcelas))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, precoFinal))
elif opcao == 4:
    totalParcelas = int(input("Quantas parcelas? "))
    precoFinal = preco + (preco * 20 / 100)
    vezes = precoFinal / totalParcelas
    print("Sua compra será parcelada em {}x de R${:.2f} SEM JUROS".format(totalParcelas, vezes))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, precoFinal))
else:
    precoFinal = 0
    print("OPÇÃO INVÁLIDA.")
