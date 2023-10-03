""" Crie duas listas em python, uma para armazenar o nome e outra lista para armazenar a idade de 5 pessoas. Posteriormente indique quais pessoas tem 18 anos ou mais e quantas pessoas são menores de idade.
Ex:
José, 10 anos
Joaquim, 19 anos
Jailton, 30 anos
Juarez, 5 anos
Joao, 18 anos
-> sao maiores de idade: Joaqui, Jailton, Joao
-> sao menores de idade: Jose, Juarez
 """

total = 5
nomes = []
idades = []

for _  in range(total):
    nome = input('Digite um nome: ')
    nomes.append(nome)
    idade = int(input('Digite sua idade: '))
    idades.append(idade)

for i in range(total):
    print(f'{nomes[i].upper()}, {idades[i]} anos')

maiores = 'São maiores de idade: '
menores = 'São menores de idade: '

for j in range(len(idades)):
    if idades[j] >= 18:
        tmp = nomes[j]
        maiores = maiores + tmp + ', '
    else:
      tmp = nomes[j]
      menores = menores + tmp + ', '

print(maiores[:-2])
print(menores[:-2])
        
         

