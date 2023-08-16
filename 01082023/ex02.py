""" 
Faça um programa que leia o nome de 5 pessoas e armazene em uma lista de nomes. No final imprima na tela uma mensagem de boas vindas para cada nome armazenada.
Ex:
nomes = ['Turing', 'Ada', 'Linus', 'Dijkstra', 'Berners-Lee']
Seja bem vindo Turing
Seja bem vindo Ada ....
 """

q_nomes = 5
nomes = []
for i in range(q_nomes):
    nome = input(f'Digite o {i+1}º nome: ')
    nomes.append(nome)

print('')

for i in range (len(nomes)):
    print(f'Seja bem-vindo(a) {nomes[i].capitalize()}!')
