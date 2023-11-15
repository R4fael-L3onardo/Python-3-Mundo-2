# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ["pedra", "papel", "tesoura"]
computador = randint(0, 2)

print("Suas opções:")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")

jogador = int(input("Qual é sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("JO!!!")
sleep(1)

print("-----------------------")
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-----------------------")

# Computador jogou PEDRA
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")

# Computador jogou PAPEL
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")

# Computador jogou TESOURA
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA!")
