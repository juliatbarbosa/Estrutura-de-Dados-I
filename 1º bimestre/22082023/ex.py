""" Escreva um programa que remova todos os elementos da primeira lista que também estão presente na segundalista """

listaA = [4,5,2,3,1,2,5] # = {1,2,3,4,5}
listaB = [3,1,5,8,9] # = {1,2,3,4}
#resultado = {2,4}
conjuntoA = set(listaA)
conjuntoB = set(listaB)
resultado = conjuntoA.difference(conjuntoB)

print(resultado)


