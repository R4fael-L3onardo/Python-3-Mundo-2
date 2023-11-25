for contador in range(0, 6):
    print("Olá")
print("Fim")
print("----")

for contador in range(0, 6, 2):
    print(contador)
print("Fim")
print("----")

numero = int(input("Digite um número: "))
for contador in range(0, numero + 1):
    print(contador)
print("Fim")
print("----")

inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
for contador in range(inicio, fim + 1, passo):
    print(contador)
print("Fim")
print("----")

soma = 0
for contador in range(0, 3):
    numero = int(input("Digite um valor: "))
    soma = soma + numero
print("A soma de todos os valores foi {}.".format(soma))
print("Fim")
print("----")
