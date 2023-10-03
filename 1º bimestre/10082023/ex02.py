""" 
2- Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor.

 """

qtd = 10
valores = []
valores_diferentes = []

for i in range(qtd):
    valor = int(input('Digite um valor: '))
    valores.append(valor)

for j in valores:
    if j not in valores_diferentes:
        valores_diferentes.append(j)

contador = len(valores_diferentes)
print(f'Valores diferentes: {contador}')