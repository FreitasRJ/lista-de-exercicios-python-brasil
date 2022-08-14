"""
Exercício 06 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0, e imprima separado o número de alunos com nota menor que 7.0 .

    >>> calcular_media([8,9,10,2],[2,10,9,5],[5,2,9,10],[10,1,1,10],[9,2,9,8],[8,8,9,7],[7,7,7,9],[4,6,5,7],[1,2,8,10],[10,2,2,8])
    Alunos com media >= 7.0: 4
    Alunos com media < 7.0: 6
    >>> calcular_media([2,1,1,2],[2,1,0,4],[3,2,5,2],[9,7,7,9],[0,6,9,2],[9,1,6,4],[10,10,9,7],[6,7,8,9],[9,8,9,6],[10,5,10,8])
    Alunos com media >= 7.0: 5
    Alunos com media < 7.0: 5
"""

import statistics
def calcular_media(*notas) -> int:
    """Escreva aqui em baixo a sua solução"""
    media_maior = 0
    for alunos in notas:
        soma = 0
        for nota in alunos:
            soma += nota
        media = soma / 4
        if media >= 7:
            media_maior += 1

    print(f'Alunos com media >= 7.0: {media_maior}')
    print(f'Alunos com media < 7.0: {10 - media_maior}')

        

'''    
    notas = []
    media_maior = 0
    for alunos in range(10):
        print(f'Entre com as notas do {alunos+1}° aluno: ')
        notas_por_aluno = []
        nota = 0
        soma = 0
        for idx in range(4):
            nota = int(input(f'Digite a {idx + 1}ª nota do aluno {alunos+1}: '))
            notas_por_aluno.append(nota)
            soma += nota
        notas.append(notas_por_aluno)
        print(notas)
        media = soma / 4
        if media >= 7:
            media_maior += 1

    print(f'Alunos com media >= 7.0: {media_maior}')
    print(f'Alunos com media < 7.0: {10 - media_maior}')
'''
#calcular_media([8,9,10,2],[2,10,9,5],[5,2,9,10],[10,1,1,10],[9,2,9,8],[8,8,9,7],[7,7,7,9],[4,6,5,7],[1,2,8,10],[10,2,2,8])