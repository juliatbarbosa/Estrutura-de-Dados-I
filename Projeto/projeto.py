
import json

estoque = {}
opcao = 1
repetir = 'S'

#Verificar se existe o arquivo na pasta, se existir, ele carrega os dados, se não, ele printa uma mensagem e ao salvar no final da execução, ele cria um novo arquivo.
try:
    with open('Projeto/estoque.json', 'r') as arquivo:
        estoque = json.load(arquivo)
except:
    print('O arquivo não existe!')

def adicionarProduto():
    codigo = input('Digite o código do produto: ')

    while codigo in estoque.keys(): # -> keys() retorna todas as chaves do estoque
        print('Código já existente. Digite novamente!')
        codigo = input('Digite o código do produto: ')

    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade de produtos: '))
    preco = float(input('Digite o preço do kg/und: '))

    # Tratativa para verificar se o produto está disponível através da quantidade disponível
    if quantidade > 0:
        disponivel = True
    else:
        disponivel = False

    #Adiciona o produto ao dicionário
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
    if estoque:
        for chave, produto in estoque.items(): # -> items() retorna os itens -> chave e valor das chaves (nome, valor...)
            print(f'Código: {chave}')
            print(f'Nome: {produto["nome"]}')
            print(f'Quantidade: {produto["quantidade"]}')
            print(f'Preço: {produto["preco"]}')
            print(f'Disponível: {"Sim" if produto["disponivel"] == True else "Não"}')
            print('='*10)
    else: 
        print('Nenhum produto existente!')

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
        for produto in estoque.values(): # values() retorna só os valores do dicionário
            produto["preco"] = produto["preco"] + (produto["preco"] * porcentagem)

    else:
        porcentagem = float(input('Digite a porcentagem que deseja descontar: ')) / 100
        for produto in estoque.values():
            produto["preco"] = produto["preco"] - (produto["preco"] * porcentagem)
            print(produto["preco"])
        
def excluirRegistroProdutoPorCodigo():
    codigo = input('Digite o código do produto: ')

    while codigo not in estoque.keys():
        print('Produto não encontrado. Digite novamente!')
        codigo = input('Digite o código do produto: ')
    
    estoque.pop(codigo) # pop() -> função para remover item do dicionario
    print(f'Produto com código {codigo} excluído com sucesso!')

while repetir == 'S':
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
    
    repetir = input('Deseja abrir o programa novamente (s/n)?  ').upper()
    opcao = 1
            
        
        