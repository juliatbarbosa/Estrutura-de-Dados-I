import json
""" Vamos supor que precisamos criar um programa para cadastrar alunos em uma escola, armazenando informações como nome, idade e nota. Podemos utilizar um dicionário para representar cada aluno, onde a chave será o número de matrícula e o valor será outro dicionário contendo as informações do aluno. """

""" 02, fulano, 19, 78 """
""" 08, beltrano, 20, 75 """

print('CADASTRO DE ALUNOS')

opcao = 1
cadastros = {}
while opcao != 3:
    print('='*10)
    print("1- Cadastrar")
    print('2- Consultar cadastros')
    print('3- Sair')
    opcao = int(input('Opcao >>>> '))
    if opcao == 1:
        print('-----Cadastrar aluno-----')
        matricula = input('Matrícula: ')
        nome = input('Nome: ')
        idade = input('Idade: ')
        nota = input('Nota: ')
        cadastro = {'nome': nome, 'idade': idade, 'nota': nota}
        cadastros[matricula] = cadastro
        print('-----Cadastrado com sucesso-----')
    elif opcao == 2:
        print('-----Alunos-----')
        print(cadastros)
        print('-----Fim dos alunos-----')
    elif opcao == 3:
        print('Salvando e saindo... 🚀')

json_str = json.dumps(cadastros)
#salvar em arquivo
with open('31082023/ex06/alunos.json', 'w') as json_file:
    json.dump(cadastros, json_file, indent=4)

