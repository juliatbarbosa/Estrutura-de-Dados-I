#ED sem repeticao, podemos tratar com uma lista
clientes = []
for i in range(10):
    nome = input ('Digite o nome:')
    if nome not in clientes:
        clientes.append(nome)
print('lista de clientes')
print (clientes)