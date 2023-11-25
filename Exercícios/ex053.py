# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando 
# os espaços. Exemplos de palíndromos:

# APOS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / ANOTARAM A DATA DA MARATONA
#                             O LOBO AMA O BOLO

frase = str(input("Digite uma frase: ")).strip().upper()
palavra = frase.split()
tudoJunto = "".join(palavra)
inverso = ""

for letra in range(len(tudoJunto) - 1, -1, -1):
    inverso = inverso + tudoJunto[letra]
print("O inverso de {} é {}.".format(tudoJunto, inverso))
if inverso == tudoJunto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
