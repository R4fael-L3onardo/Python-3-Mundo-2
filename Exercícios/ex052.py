# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número: "))
total = 0

for contador in range(1, numero + 1):
    if numero % contador == 0:
        print("\033[32m", end=" ")
        total = total + 1
    else:
        print("\033[31m", end=" " )
    print(contador, end=" ")
print("\n\033[mO número {} foi divisível {} vezes".format(numero, total))

if total == 2:
    print("E por isso ele É PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")
