# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte 
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal 
# não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anosFinanciamento = int(input("Quantos anos de financiamento? "))

valorPrestacao = valorCasa / (anosFinanciamento * 12)
porcetagemSalario = (30 * salario) / 100

print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(valorCasa, anosFinanciamento, valorPrestacao))

if valorPrestacao > porcetagemSalario:
    print("Empréstimo Negado!")
else:
    print("Empréstimo pode ser Concedido!")
