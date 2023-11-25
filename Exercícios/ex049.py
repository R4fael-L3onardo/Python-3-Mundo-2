# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora 
# utilizando um laço for.

numero = int(input("Digite um número para ver sua tabuada: "))
vezes = 0
for contador in range(1, 11):
    vezes = vezes + 1
    tabuada = numero * contador
    print("{} x {:2} = {}".format(numero, vezes, tabuada))
