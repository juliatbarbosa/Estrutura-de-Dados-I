""" 
4- Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que simule o lançamento do dado e determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos.
"""

import random

lancamentos = 50
dado = 6
ocorrencias = 0

for _ in range(lancamentos):
    if random.randint(1, 6) == dado:
        ocorrencias += 1

percentual_ocorrencias = (ocorrencias / lancamentos) * 100

print(f"Percentual de ocorrências da face {dado}: {percentual_ocorrencias:.2f}%")