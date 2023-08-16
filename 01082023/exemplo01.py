""" 
Listas - > Vetor (array)
Lista (são Ed dinâmicas -> aumenta ou diminui de tamanho de acordo com os dados armazenados)
Vetor ( são ED estáticas -> mantém o tamanho fixo)
No pyhton -> não tem vetor
 """

numeros = [1,4,9,16,25]
numeros[1] = 6 #substitui o valor na posição 1 por 6 

#---------------------------------------#

#pegar último elemento
numeros[-1]
#ou
numeros[len(numeros) - 1]

#---------------------------------------#

#união de listas

outra_lista = [36,49,64]

nova_lista = numeros + outra_lista
print(nova_lista)

#---------------------------------------#

#adicionar novos elementos na lista

nova_lista.append(9*9)
print(nova_lista)

#---------------------------------------#

#corrigir o elemento na posição 1

nova_lista[1] = 2**2
print(nova_lista)

#---------------------------------------#

#percorrer a lista exibindo apenas os valores

for valor in nova_lista:
    print(valor)

#trazer o indice e valor
for indice in range(len(nova_lista)):
    valor = nova_lista[indice]
    print(f'Índice= {indice} e valor {valor}')
print('----------OU------------')
for indice, valor in enumerate(nova_lista):
    print(f'Índice= {indice} e valor {valor}')