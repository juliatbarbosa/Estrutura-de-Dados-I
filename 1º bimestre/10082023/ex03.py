""" 
3- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) aparece pela primeira vez no vetor. Caso o valor x não seja encontrado, o programa deve imprimir o valor -1
 """

qtd = 5
valores = []

for i in range(qtd):
    valor = int(input('Digite um valor: '))
    valores.append(valor)

valorX = int(input('Digite um valor X: '))


if valorX in valores:
    print(f'{valores.index(valorX)}º posição')
else:
    print('Posição: -1')
