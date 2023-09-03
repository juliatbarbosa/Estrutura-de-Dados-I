import json
#r - abrir para leitura
#w - abrir para escrita (sobrescreve)
#a - abrir para escrita (anexa no fim)
with open('31082023/dados.json', 'r') as arquivo:
    registros = json.load(arquivo)

print(registros)