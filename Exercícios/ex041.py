# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
anoAtual = date.today().year

anoNascimento = int(input("Ano de Nascimento: "))

idadeAtleta = anoAtual - anoNascimento

print("O atleta tem {} anos.".format(idadeAtleta))

if idadeAtleta <= 9:
    print("Classificação: MIRIM")
elif idadeAtleta <= 14:
    print("Classificação: INFANTIL")
elif idadeAtleta <= 19:
    print("Classificação: JÚNIOR")
elif idadeAtleta <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")
