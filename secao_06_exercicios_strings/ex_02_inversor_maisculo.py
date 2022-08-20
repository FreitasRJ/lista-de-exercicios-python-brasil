"""
Exercício 02 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Faça um programa que mostre o nome do usuário de trás para frente utilizando somente
letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar
letras maiúsculas ou minúsculas.


    >>> inversor('lucca')
    'ACCUL'
    >>> inversor('douglas')
    'SALGUOD'
    >>> inversor('TaTIana')
    'ANAITAT'
    >>> inversor('MARIa')
    'AIRAM'

"""


def inversor(nome: str) -> str:
    """ Escreva seu código aqui embaixo """
    nome = nome.upper()
    tam = len(nome)
    invertido = ""
    for idx in range(tam, 0,-1):
        invertido += nome[idx-1]
    print(f"'{invertido}'")

#inversor('MARIa')
