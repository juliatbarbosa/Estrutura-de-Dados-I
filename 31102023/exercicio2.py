""" 
2. Faça uma função que informe o status do aluno a partir da sua média de acordo com a tabela a seguir:
— Nota acima de 6 → "Aprovado"
— Nota entre 4 e 6 → "Verificação Suplementar"
— Nota abaixo de 4 → "Reprovado" 
 """

media = float(input('Digite sua média: '))

def status(media):
    if (media > 6):
        return 'Aprovado'
    elif (media >= 4 and media <= 6 ):
        return "Verificação Suplementar"
    else:
        return "Reprovado"

print(status(media))
