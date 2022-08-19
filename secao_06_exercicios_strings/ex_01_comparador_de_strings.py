"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Tamanho de strings. Faça um programa que compare 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings


    >>> comparar('Brasil Hexa 2006', 'Brasil! Hexa 2006!')
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
    >>> comparar('Igual', 'Igual')
    String 1: Igual
    String 2: Igual
    Tamanho de "Igual": 5 caracteres
    Tamanho de "Igual": 5 caracteres
    As duas strings possuem  mesmo tamanho.
    As duas strings possuem conteúdo igual.

"""


def comparar(s1: str, s2: str):
    """Escreva aqui em baixo a sua solução"""
    tam_s1 = len(s1)
    tam_s2 = len(s2)
    if (tam_s1 == tam_s2) and s1 is s2:
        men_1 = men_2 = 'Igual'
        mensagem_final = 'As duas strings possuem  mesmo tamanho.\nAs duas strings possuem conteúdo igual.'
    else:
        men_1 = s1
        men_2 = s2

        if tam_s1 != tam_s2:
            mensagem_final = 'As duas strings são de tamanhos diferentes.\n'
        else:
            mensagem_final = 'As duas strings possuem  mesmo tamanho.\n'

        mensagem_final += 'As duas strings possuem conteúdo diferente.'

       
    print(f'String 1: {men_1}')
    print(f'String 2: {men_2}')

    print(f'Tamanho de "{men_1}": {tam_s1} caracteres')
    print(f'Tamanho de "{men_2}": {tam_s2} caracteres')

    print(mensagem_final)
   


