import random
# criar uma matriz N X M preenchidas com zeros
# N -> numero de linha
# M -> numero de colunas
# E imprimir na forma de matriz
N = 4
M = 5

###### EXERCICIO #####
# ADICIONE ELEMENTOS DE FORMA ALEATORIA EM UMA MATRIZ NxM E RETORNE A QUANTIDADE DE NUMEROS PARES!

matriz = []

for linha in range(N):
    matriz.append([random.randint(1, 100) for _ in range(M)])

numeros_pares = 0
for linha in matriz:
    for elemento in linha:
        print(elemento, end='\t')
        if (elemento % 2 == 0 ):
            numeros_pares += 1
    print()

print("\nQuantidade de números pares na matriz:", numeros_pares)