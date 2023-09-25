import json
""" 
produto - frutas
atributos: nome, codigo, preco, peso
    chave: codigo
    valor: nome, preco, peso
"""

banco_dados = {}
opcao = 1

def carregarDados():
    try:
        with open('05092023/estoque.json', 'r') as arquivo:
            banco_dados = json.load(arquivo)
    except:
        print('O arquivo não existe!')

# preciso carregar o que estiver no arquivo
carregarDados()

while opcao != 4:
    print('='*10)
    print("1- Adicionar")
    print('2- Consultar por código')
    print('3- Consultar todos')
    print('4- Sair')
    opcao = int(input('Escolha a opção: '))
    if opcao == 1:
        print('-----Cadastrar produto -----')
        codigo = input('Digite o código: ')
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do kg/und: '))
        
        banco_dados[codigo] = {'nome': nome, 'preco': preco}
        with open('05092023/estoque.json', 'w') as arquivo:
            json.dump(banco_dados, arquivo, indent=4)
    elif opcao == 2:
        print('-----Consultar por código-----')
    elif opcao == 3:
        print('-----Consultar todos-----')
    elif opcao == 4:
        print('Salvando e saindo... 🚀')
    else:
        print('Opção inválida!')

