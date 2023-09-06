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