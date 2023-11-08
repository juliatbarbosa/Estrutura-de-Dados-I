import math

""" 1. O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M)
alunos. Faça o programa que lê o valor de Ne Me informa o número de combinações possíveis
— Número de combinações é igual a N!/(M! * (N-M)!)
— Use funções para evitar repetição de código
"""
n = int(input('Digite o número de alunos: '))
m = int(input('Digite o número de alunos do primeiro grupo: '))

total = math.factorial(n)/(math.factorial(m) * math.factorial(n-m))
print(f'O número de combinações possíveis é: {total:.0f}')