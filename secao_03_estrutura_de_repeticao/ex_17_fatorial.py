"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

    >>> calcular_fatorial(0)
    1
    >>> calcular_fatorial(1)
    1
    >>> calcular_fatorial(2)
    2
    >>> calcular_fatorial(3)
    6
    >>> calcular_fatorial(4)
    24
    >>> calcular_fatorial(5)
    120

"""


def calcular_fatorial(n: int) -> int:
    """Escreva aqui em baixo a sua solução"""
    
    try:
        #n = int(input('Entre com o número que deseja saber o fatorial: '))
        if n == 0:
            res = 1
        else: 
            res = n
            for a in range(n,2,-1):
                res = res * (a - 1)

        print(res)
    except ValueError:
        print('Entrada inválida!!!')

#calcular_fatorial(5)