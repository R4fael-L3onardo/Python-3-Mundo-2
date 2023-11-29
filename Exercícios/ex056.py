# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres 
# têm menos de 20 anos.

somaIdade = 0
mediaIdade = 0
maisVelho = 0
nomeMaisVelho = ""
menos20anos = 0

for contador in range(1,5):
    print("---- {}° PESSOA ----".format(contador))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()

    somaIdade = somaIdade + idade
    mediaIdade = somaIdade / 4

    if contador == 1 and sexo in "Mm":
        maisVelho = idade
        nomeMaisVelho = nome
    if sexo in "Mm" and idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nome

    if sexo in "Ff" and idade < 20:
        menos20anos = menos20anos + 1

print("A média de idade do grupo é de {} anos.".format(mediaIdade))
print("O homem mais velho tem {} e se chama {}.".format(maisVelho, nomeMaisVelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(menos20anos))
