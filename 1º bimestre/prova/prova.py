import json

banco_dados = {}

with open('dados_prova.json', 'r') as arquivo:
        banco_dados = json.load(arquivo)

nomes = []
maior_idade = []
menor_idade = []
salario_maior = []
salario_menor = []

print('Funcionarios')
for chave in banco_dados:
    nomes.append(banco_dados[chave]["nome"])

for i in sorted(nomes):
          print(i)
print('\nMaior idade')
for chave in banco_dados:
       maior_idade.append(banco_dados[chave]["idade"])
for i in banco_dados:
       if banco_dados[i]["idade"] == max(maior_idade):
            print(f'{i}: Nome: {banco_dados[i]["nome"]}, idade: {banco_dados[i]["idade"]}, salário: {banco_dados[i]["salario"]}')
print('\nMenor idade')
for chave in banco_dados:
       menor_idade.append(banco_dados[chave]["idade"])
for i in banco_dados:
       if banco_dados[i]["idade"] == min(menor_idade):
            print(f'{i}: Nome: {banco_dados[i]["nome"]}, idade: {banco_dados[i]["idade"]}, salário: {banco_dados[i]["salario"]}')

print('\nSalário maior')
for chave in banco_dados:
       salario_maior.append(banco_dados[chave]["salario"])
for i in banco_dados:
       if banco_dados[i]["salario"] == max(salario_maior):
            print(f'{i}: Nome: {banco_dados[i]["nome"]}, idade: {banco_dados[i]["idade"]}, salário: {banco_dados[i]["salario"]}')

print('\nSalário menor')
for chave in banco_dados:
       salario_menor.append(banco_dados[chave]["salario"])
for i in banco_dados:
       if banco_dados[i]["salario"] == min(salario_menor):
            print(f'{i}: Nome: {banco_dados[i]["nome"]}, idade: {banco_dados[i]["idade"]}, salário: {banco_dados[i]["salario"]}')


