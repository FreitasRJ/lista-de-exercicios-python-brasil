"""
Exercício 26 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

uma eleição existem três candidatos. Faça um programa que peça o número total
 de eleitores. Peça para cada eleitor votar
 e ao final mostrar o número de votos de cada candidato.

    >>> calcular_votos()
    Votantes: 0
    Votos no candidato corrupto: 0
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto')
    Votantes: 1
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso')
    Votantes: 2
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 3
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 1
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz', 'corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 6
    Votos no candidato corrupto: 2
    Votos no candidato mentiroso: 2
    Votos no candidato rouba, mas faz: 2

"""


def calcular_votos(*votos):
    """Escreva aqui em baixo a sua solução"""

    corrupto_votos = 0
    mentiroso_votos = 0
    rouba_votos = 0
    votantes = len(votos)
    
    for voto in votos:
        if voto == 'corrupto':
            corrupto_votos += 1

        elif voto == 'mentiroso':
            mentiroso_votos += 1
        
        elif voto == 'rouba, mas faz':
            rouba_votos += 1
    mensagem = f'Votantes: {votantes}\n'
    mensagem += f'Votos no candidato corrupto: {corrupto_votos}\n'
    mensagem += f'Votos no candidato mentiroso: {mentiroso_votos}\n'
    mensagem += f'Votos no candidato rouba, mas faz: {rouba_votos}'

    return print(mensagem)

#calcular_votos('corrupto', 'mentiroso')   