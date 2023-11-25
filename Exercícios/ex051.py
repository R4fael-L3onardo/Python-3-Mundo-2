# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

print("10 TERMOS DE UMA PA")

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10 - 1) * razao

for contador in range(termo, decimo + razao, razao):
            print(contador, end=" -> ")
print("ACABOU")
