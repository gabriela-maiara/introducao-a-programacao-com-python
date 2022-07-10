materia1 = float(input('Qual é a nota da primeira matéria: '))
materia2 = float(input('Qual é a nota da segunda matéria: '))
materia3 = float(input('Qual é a nota da terceira matéria: '))
media = 7
if (materia1 >= media) and (materia2 >= media) and (materia3 >= media):
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')