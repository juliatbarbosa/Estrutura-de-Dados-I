""" 
[codigo, nome, descricao, preco]
ATRIBUTOS OU CARACTERISTICAS--›codigo, nome, descricão, preco
CHAVE-> codigo
VALOR-> nome, descricao, preco. Vamos selecionar uma caracteristica nome.
codigo: nome
 """
estoque = {} #Ed dicionario
opcao = 1
while opcao != 3:
    print('=' * 10)
    print('===MENU===')
    print('1- Adicionar')
    print('2- Consultar')
    print('3- Sair')
    opcao =int(input('>>>>'))
    if opcao == 1:
        codigo = input('Código: ')
        nome = input('Nome do produto: ')
        estoque[codigo] = nome
        print('Adicionado com sucesso!')
    elif opcao == 2:
        #vou informar o codigo e ele irá me retornar o nome
        codigo = input('Código desejado: ')
        #verificar se chave está no estoque
        if codigo in estoque:
            registro = estoque[codigo]
            print(f'REGISTRO RECUPERADO: {registro}')
        else:
            print('Produto não encontrado')
    elif opcao == 3:
        print('saindo....')