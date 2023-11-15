# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")
opcao = int(input(("Sua opção: ")))

if opcao == 1:
    binario = bin(numero)
    print("{} convertido para BINÁRIO é igual a {}".format(numero, binario[2:]))
elif opcao == 2:
    octal = oct(numero)
    print("{} convertido para OCTAL é igual a {}".format(numero, octal[2:]))
elif opcao == 3:
    hexadecimal = hex(numero)
    print("{} convertido para HEXADECIMAL é igual a {}".format(numero, hexadecimal[2:]))
else:
    print("Opção inválida. Tente novamente.")
