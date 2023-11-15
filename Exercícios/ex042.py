# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo 
# será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

primeiro = float(input("Primeiro segmento: "))
segundo = float(input("Segundo segmento: "))
terceiro = float(input("Terceiro segmento: "))

if (primeiro + segundo) > terceiro and (primeiro + terceiro) > segundo and (terceiro + segundo) > primeiro:
    print("Os segmentos acima PODEM FORMAR um triângulo ",end="")
    if primeiro == segundo == terceiro:
        print("EQUILÁTERO!")
    elif primeiro != segundo != terceiro != primeiro:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos acima Não Podem Formar um triângulo!")
