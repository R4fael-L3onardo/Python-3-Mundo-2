# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que 
# forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
vezes = 0
for contador in range(1, 7):
    numero = int(input("Digite {}° valor: ".format(contador)))
    if numero % 2 == 0:
        vezes = vezes + 1
        soma = soma + numero
print("Você informou {} números pares e a soma foi {}.".format(vezes, soma))
