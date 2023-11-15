# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já
# passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou 
# que passou do prazo.

from datetime import date
anoAtual = date.today().year

anoNascimento = int(input("Ano de nascimento: "))

idadeAlistamento = 18
idadeAtual = anoAtual - anoNascimento
print("Quem nasceu em {} tem {} anos em {}.".format(anoNascimento, idadeAtual, anoAtual))

if idadeAtual < idadeAlistamento:
    anosFaltam = idadeAlistamento - idadeAtual
    if anosFaltam != 1:
        print("Ainda faltam {} anos para o alistamento.".format(anosFaltam))
    if anosFaltam == 1:
        print("Ainda falta {} ano para o alistamento.".format(anosFaltam))
    anoAlistamento = anoAtual + anosFaltam
    print("Seu alistamento será em {}.".format(anoAlistamento))

elif idadeAtual > idadeAlistamento:
    deveriaSeAlistado = idadeAtual - idadeAlistamento
    if deveriaSeAlistado != 1:
        print("Você já deveria ter se alistado há {} anos.".format(deveriaSeAlistado))
    if deveriaSeAlistado == 1:
        print("Você já deveria ter se alistado há {} ano.".format(deveriaSeAlistado))
    anoAlistamento = anoAtual - deveriaSeAlistado
    print("Seu alistamento foi em {}.".format(anoAlistamento))

else:
    print("Você tem que se alistar IMEDIATAMENTE!")
