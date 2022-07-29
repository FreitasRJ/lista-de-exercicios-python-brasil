"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(n1, n2, n3):
    """Escreva aqui em baixo a sua solução"""
    if round(n1) == n1:
        n1 = round(n1)
    if round(n2) ==n2:
        n2 = round(n2)
    if round(n3) == n3:
        n3 = round(n3)    
                  
    if n1 < n3:
        n1, n3 =  n3, n1 
    if n1 < n2:
        n1, n2 = n2, n1 
    if n2 < n3:
        n2, n3 = n3, n2

    return print(f'{n1}, {n2}, {n3}')
#ordenar_decrescente(2,3,5)    