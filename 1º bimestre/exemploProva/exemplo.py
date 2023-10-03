""" ############ LISTAS ################ """

numeros = [1,4,9,16,25]
numeros[1] = 6 #substitui o valor na posição 1 por 6 
#---------------------------------------#
#pegar último elemento
numeros[-1]
#ou
numeros[len(numeros) - 1]
#---------------------------------------#
#união de listas
outra_lista = [36,49,64]
nova_lista = numeros + outra_lista
print(nova_lista)
#---------------------------------------#
#adicionar novos elementos na lista
nova_lista.append(9*9)
print(nova_lista)
#---------------------------------------#
#corrigir o elemento na posição 1
nova_lista[1] = 2**2
print(nova_lista)
#---------------------------------------#
#percorrer a lista exibindo apenas os valores
for valor in nova_lista:
    print(valor)
#trazer o indice e valor
for indice in range(len(nova_lista)):
    valor = nova_lista[indice]
    print(f'Índice= {indice} e valor {valor}')
print('----------OU------------')
for indice, valor in enumerate(nova_lista):
    print(f'Índice= {indice} e valor {valor}')
#---------------------------------------#
#exemplos
lista = [9,7,4,5]
del lista[1]  # remove o elemento da posicao 1
#print(lista) -> [9, 4, 5]
lista.append(8) # adiciona elemento no fim da lista
#print(lista) -> [9, 4, 5, 8]
lista.insert(1, 3) # insere elemento 3 na posicao 1
#print(lista)[9, 3, 4, 5, 8]
valor = lista.pop(2)   # retorna e retira elemento do indice 2
#print(valor) -> 4
#print(lista) -> [9, 3, 5, 8]
lista.sort() ## ordenar a lista
#print(lista)->[3, 5, 8, 9]


""" ############ TUPLAS ################ """

""" Uma tupla é uma lista imutável, ou seja, uma tupla é uma sequência que não pode ser alterada depois de criada. Uma tupla é definida de forma parecida com uma lista com a diferença do delimitador. Enquanto listas utilizam colchetes como delimitadores, as tuplas usam parênteses """
dias_semana = ('dom','seg', 'ter', 'qua', 'qui', 'sex', 'sab')

tupla1 = (4,6)
tupla2 = (2,5)
tupla3 = tupla1 + tupla2   # concatenar duas tuplas
print(tupla3)
(4, 6, 2, 5)

tupla4 = tupla1*tupla2 # erro

tupla4 = tupla1*8     # repete a tupla 8 vezes
print(tupla4)
(4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6)

print(tupla1)
print(tupla2)
(4, 6)
(2, 5)

# vc deseja obter tupla_soma = (6,11) = (4+2, 6+5)
tupla_soma = (tupla1[0]+tupla2[0], tupla1[1]+tupla2[1])
print(tupla_soma)
(6, 11)

print(dias_semana)
('dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab')
for indice, dia in enumerate(dias_semana):
    print(f'{indice} - {dia}')
""" 0 - dom
1 - seg
2 - ter
3 - qua
4 - qui
5 - sex
6 - sab """
for indice in range(len(dias_semana)):
    dia = dias_semana[indice]
    print(f'{indice} - {dia}')
""" 0 - dom
1 - seg
2 - ter
3 - qua
4 - qui
5 - sex
6 - sab """
dias_semana_lista = list(dias_semana)
print(dias_semana_lista)
['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
print(type(dias_semana_lista))
print(type(dias_semana))
""" <class 'list'>
<class 'tuple'> """

""" ############ DICIONÁRIO ################ """
""" ED chave-valor, onde cada elemento e' composto por uma chave unica e seu respectivo valor.

chave - algo que identifica um registro, e essa chave seja unica.

cliente que possui o cpf, o cpf poderia ser a chave.
dados do cliente (nome, endereco, data nascimento, saldo, etc.) o valor.
Os dicionarios sao uteis para armazenar e recuper informacoes de forma eficiente. O acesso aos valores e' realizado por meio de suas chaves, e nao por meio de indice como nas listas. """

clientes = {}    # dicionario por meios do simbolo de {}

print(type(clientes))
#<class 'dict'>

clientes['000.000.000-00'] = ['Joaquim', 20]
print(clientes)
{'000.000.000-00': ['Joaquim', 20]}

clientes['111.111.111-11'] = 'Tereza'
print(clientes)
{'000.000.000-00': ['Joaquim', 20], '111.111.111-11': 'Tereza'}

# recuperar apenas o registro com cpf 111.111.111-11
valor = clientes['111.111.111-11']
print(valor)
#Tereza

# recuperar o registro com cpf 000.000.000-00
valor = clientes['000.000.000-00']
print(valor)
['Joaquim', 20]

chaves = clientes.keys()
print(chaves)
#dict_keys(['000.000.000-00', '111.111.111-11'])

for cpf in clientes.keys():
    print(f"CPF: {cpf}")
    valor = clientes[cpf]
    print(valor)
""" CPF: 000.000.000-00
['Joaquim', 20]
CPF: 111.111.111-11
Tereza """

for cpf, valor in clientes.items():
    print(f"CPF: {cpf}")
    valor = clientes[cpf]
    print(valor)
""" CPF: 000.000.000-00
['Joaquim', 20]
CPF: 111.111.111-11
Tereza """

# outra forma criar um dicionario
produtos = {'mouse': {'cor': 'preto', 'preco': 65.99}, 'teclado': {'cor':'branco', 'preco':70}}
print(produtos)
{'mouse': {'cor': 'preto', 'preco': 65.99}, 'teclado': {'cor': 'branco', 'preco': 70}}

produtos['mouse']['cor']
'preto'

produtos['teclado']
{'cor': 'branco', 'preco': 70}

produtos['teclado']['cor']
'branco'

dicionario = {'000256':'Alysson'}
dicionario['000256']
'Alysson'

dicionario['000100'] = 'Dorival'
print(dicionario)
{'000256': 'Alysson', '000100': 'Dorival'}

dicionario['000256'] = 'francisco'
print(dicionario)
{'000256': 'francisco', '000100': 'Dorival'}

dicionario.items()
#dict_items([('000256', 'francisco'), ('000100', 'Dorival')])

exemplos = {}
exemplos[3]='Joaquim'
exemplos
{3: 'Joaquim'}

exemplos[0] = 'Maria'

produtos
{'mouse': {'cor': 'preto', 'preco': 65.99},
 'teclado': {'cor': 'branco', 'preco': 70}}

'carro' in produtos
False
'mouse' in produtos
True


#EXEMPLO PROJETO

#### Verificar com o Alysson se ao adicionar precisa de quantidade e se está disponível ####
#### Tenho que salvar apenas quando apertar pra salvar e sair?

import json

estoque = {}
opcao = 1

try:
    with open('Projeto/estoque.json', 'r') as arquivo:
        estoque = json.load(arquivo)
except:
    print('O arquivo não existe!')

def adicionarProduto():
    codigo = input('Digite o código do produto: ')

    while codigo in estoque.keys():
        print('Código já existente. Digite novamente!')
        codigo = input('Digite o código do produto: ')

    nome = input('Digite o nome do produto: ')
    quantidade = input('Digite a quantidade de produtos: ')
    preco = float(input('Digite o preço do kg/und: '))
    disponivel = input('Produto disponivel (S/N): ').upper()

    # Tratativa para transformar a entrada do usuário em valor booleano
    if disponivel == "S":
        disponivel = True
    else:
        disponivel = False

    estoque[codigo] = {'nome': nome, 'quantidade': quantidade, 'preco': preco, 'disponivel': disponivel}

def consultarProdutoPorCodigo():
    codigo = input('Digite o código do produto: ')

    # Enquanto não existir um produto com o código digitado no estoque, peça um novo código
    while codigo not in estoque.keys(): # -> retorna uma lista com todas as chaves do dicionário
        print('Produto não encontrado. Digite novamente!')
        codigo = input('Digite o código do produto: ')

    print('Produto encontrado!')

    print(f'Nome: {estoque[codigo]["nome"]}')
    print(f'Quantidade: {estoque[codigo]["quantidade"]}')
    print(f'Preço: {estoque[codigo]["preco"]}')
    print(f'Disponível: {estoque[codigo]["disponivel"]}')

def consultarTodosProdutos():
    for chave, produto in estoque.items(): # -> retorna um par = chave e valor
        print(f'Código: {chave}')
        print(f'Nome: {produto["nome"]}')
        print(f'Quantidade: {produto["quantidade"]}')
        print(f'Preço: {produto["preco"]}')
        print(f'Disponível: {"Sim" if produto["disponivel"] == True else "Não"}')
        print('='*10)

def alterarPrecoPorCodigo():
    codigo = input('Digite o código do produto: ')

    # Enquanto não existir um produto com o código digitado no estoque, peça um novo código
    while codigo not in estoque.keys(): # -> retorna uma lista com todas as chaves do dicionário
        print('Produto não encontrado. Digite novamente!')
        codigo = input('Digite o código do produto: ')

    precoAtual = estoque[codigo]["preco"]
    print(f'Preço atual: R$ {precoAtual:.2f}')

    novoPreco = float(input('Digite o novo preço: '))
    estoque[codigo]["preco"] = novoPreco

    print('Preço alterado com sucesso!')
    
def addAcrescimoOuDescontoTodosProdutos():
    aplicacao = input('Deseja aplicar um acréscimo ou desconto em todos os produtos (ACRESCIMO/DESCONTO): ').upper()

    # Enquanto aplicação for diferente de acrescimo e de desconto, peça uma nova aplicacao
    while aplicacao != 'ACRESCIMO' and aplicacao != 'DESCONTO':
        print('Opção inválida. Digite novamente!')
        aplicacao = input('Deseja aplicar um acréscimo ou desconto em todos os produtos (ACRESCIMO/DESCONTO): ').upper()

    if aplicacao == 'ACRESCIMO':
        porcentagem = float(input('Digite a porcentagem que deseja acrescentar: ')) / 100
        for produto in estoque.values():
            produto["preco"] = produto["preco"] + (produto["preco"] * porcentagem)

    else:
        porcentagem = float(input('Digite a porcentagem que deseja descontar: ')) / 100
        for produto in estoque.values():
            produto["preco"] = round(produto["preco"] - (produto["preco"] * porcentagem), 2) # round usada para limitar as casas decimais
            print(produto["preco"])
        
def excluirRegistroProdutoPorCodigo():
    codigo = input('Digite o código do produto: ')

    while codigo not in estoque.keys():
        print('Produto não encontrado. Digite novamente!')
        codigo = input('Digite o código do produto: ')
    
    estoque.pop(codigo)
    print(estoque)

while opcao != 7:
    print('='*10)
    print("1- Adicionar")
    print('2- Consultar por código')
    print('3- Consultar todos')
    print('4- Alterar preço de um produto')
    print('5- Aplicar um acréscimo ou desconto em todos os produtos')
    print('6- Excluir um registro de produto')
    print('7- Salvar e sair')

    opcao = int(input('Escolha a opção: '))

    if opcao == 1:
        print('-----Adicionar um novo produto -----')
        adicionarProduto()
        
    elif opcao == 2:
        print('-----Consultar por código-----')
        consultarProdutoPorCodigo()

    elif opcao == 3:
        print('-----Consultar todos-----')
        consultarTodosProdutos()

    elif opcao == 4:
        print('-----Alterar preço de um produto-----')
        alterarPrecoPorCodigo()

    elif opcao == 5:
        print('-----Aplicar um acréscimo ou desconto em todos os produtos-----')
        addAcrescimoOuDescontoTodosProdutos()

    elif opcao == 6:
        print('-----Excluir um registro de produto-----')
        excluirRegistroProdutoPorCodigo()

    elif opcao == 7:
        print('Salvando e saindo... 🚀')

        with open('Projeto/estoque.json', 'w') as arquivo:
            json.dump(estoque, arquivo, indent=4)
    else:
        print('Opção inválida!')

        
import json

#r - abrir para leitura
#w - abrir para escrita (sobrescreve)
#a - abrir para escrita (anexa no fim)

with open('31082023/dados.json', 'r') as arquivo:
    registros = json.load(arquivo)
print(registros)

with open('05092023/estoque.json', 'w') as arquivo:
            json.dump(banco_dados, arquivo, indent=4)


try:
    with open('05092023/estoque.json', 'r') as arquivo:
            banco_dados = json.load(arquivo)
except:
    print('O arquivo não existe!')

import json

reg01={'nome': "Fulano", 'idade': 10, 'matriculado': True}
reg02={'nome': "Beltrano", 'idade': 12, 'matriculado': False}


dados = {"alunos": [reg01,reg02]}
print('DICIONÁRIO PYTHON')
print(dados)
#serializa o dicionario para json
json_str = json.dumps(dados)
print('STRING SERIALIZADA - FORMATO JSON')
print(json_str)
#salvar em arquivo
with open('31082023/dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)
