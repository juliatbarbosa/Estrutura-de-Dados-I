""" 
Utilizando listas ou tuplas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"
 """

"""  tupla, um for com um if else com sim ou não"""

perguntas = ("Telefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? ","Já trabalhou com a vítima? ")
sim = 0
for i in range(len(perguntas)):
    resp = input(perguntas[i] + 'Sim ou Não')
    if resp.upper() == 'SIM':
        sim = sim+1
if sim == 2:
    print( 'Pessoa suspeita')
elif sim == 3 or sim == 4 :
    print( 'Cúmplice')
elif sim == 5:
    print( 'Assassino')
else: 
   print( 'Inocente')