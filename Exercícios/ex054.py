# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas 
# pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoAtual = date.today().year
maiorDeIdade = 0
menorDeIdade = 0

for contador in range(1, 8):
    dataNascimento = int(input("Em que ano a {}° pessoa nasceu? ".format(contador)))
    idade = anoAtual - dataNascimento
    if idade >= 21:
        maiorDeIdade = maiorDeIdade + 1
    else:
        menorDeIdade = menorDeIdade + 1
        
print("Ao todo tivemos {} pessoas maiores de idade.".format(maiorDeIdade))
print("E também  tivemos {} pessoas menores de idade.".format(menorDeIdade))
