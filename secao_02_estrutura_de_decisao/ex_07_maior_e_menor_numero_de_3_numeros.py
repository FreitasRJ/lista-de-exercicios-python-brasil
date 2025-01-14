"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(a, b, c):
    """Escreva aqui em baixo a sua solução"""
    if a > b:
        a,b = b,a
    if b > c:
        b,c = c,b
    if a > c:
        a,c = c,b
    if a > b:
        a,b = b,a
    menor = a
    maior = c
    return print(f'Maior: {maior}\n' + f'Menor: {menor}')
#calcular_maior_de_3_numeros(7, 3, 4)