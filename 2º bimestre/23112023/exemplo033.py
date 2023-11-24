matriz = []
N = 4
M = 5
for lin in range(N):
    colunas = []
    for col in range(M):
        colunas.append(2*lin + 3*col*col)
    matriz.append(colunas)
print(matriz)

######################################################

def f(x):
    return x**2 + 7 *x - 4

matriz = []
N = 4
M = 5
for lin in range(N):
    colunas = []
    for col in range(M):
        colunas.append(f(lin*col))
    matriz.append(colunas)
print(matriz)