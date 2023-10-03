#Estruturas de dados

notas = [8.0, 5.5, 1.5]
#tam = len(notas) -> legth - comprimento do arrey
#print(notas[3]) -> índice inválido (não existe na lista)
media = (notas[0] + notas[1] + notas[2]) / 3
print(f'Média = {media}')
media2 = (notas[0] + notas[1] + notas[2]) / len(notas)
print(f'Média = {media2}')


print('---FOR---')
notas2 = [8.0, 5.5, 1.5, 9, 10]
soma = 0
for indice in range(len(notas2)):
    print(indice, end = ' >>>> ')
    print(notas2[indice])
    soma = soma + notas2[indice]
    #print(soma)

media3 = soma/len(notas2)
print(f'Média final = {media3}')

#---------------------------------------------------------------------#
nomes=[]
for i in range(10):
    tmp = input(f"digite o nome {i}: ")
    nomes.append(tmp) # adiciona valor na lista

print(nomes)