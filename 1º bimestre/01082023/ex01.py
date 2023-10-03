"""
Armazenar as notas de 10 alunos em uma lista. A
nota de cada aluno será informada pelo teclado.
"""

n_alunos = 10
notas = []
for i in range(n_alunos):
    nota = float(input('Digite sua nota: '))
    notas.append(nota)
    print(notas)

media = sum(notas)/len(notas)
print(f'Média final= {media}')

# sum - soma dos valores presente na lista
# len - a quantidade de valores presente na lista


