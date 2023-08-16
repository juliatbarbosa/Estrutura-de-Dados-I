""" 
Exercício 01 - 10/08/2023
Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo
 """

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
pares = []
negativos = []
contador = 0

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])

for i in range(len(lista)):
    if lista[i] < 0:
        negativos.append(lista[i])


for i in range(len(lista)):
    if lista[i] == lista[0]:
        contador+=1


    

print(f'Maior elemento: {max(lista)}')
print(f'Menor elemento: {min(lista)}')
print(f'Números pares: {pares}')
print(f'Número de ocorrências do primeiro elemento da lista: {contador}')
print(f'Média dos elementos: {(sum(lista)/len(lista)):.2f}')
print(f'Soma dos elementos de valor negativo: {sum(negativos)}')