"""
Exercício 07 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia 5 números e informe o maior número.

    >>> calcular_maior_numero(1, 2, 3, 4, 5)
    5
    >>> calcular_maior_numero(-1, -30, -20, -15, -2)
    -1
"""




def calcular_maior_numero(n1: int, n2: int, n3: int, n4: int, n5: int,) -> int:
    """Escreva aqui em baixo a sua solução""" 

    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5
    print(maior)


'''
 Minha resposta original. Abandonada por não passar no doctest do curso
    try:
        maior = 0
        for a in range(1,6):
            numero = int(input(f'Informe o número {a}:  '))
            if numero > maior:
                maior = numero

        print(f'O maior número da lista é: {maior}')
    except ValueError:
        print('Entrada inválida!!!')
#calcular_maior_numero(1, 2, 3, 4, 5)
'''