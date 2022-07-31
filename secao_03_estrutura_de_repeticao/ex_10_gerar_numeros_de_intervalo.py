"""
Exercício 10 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido.

    >>> calcular_numeros_no_intervalo(1, 10)
    '1, 2, 3, 4, 5, 6, 7, 8, 9'
    >>> calcular_numeros_no_intervalo(-10, -1)
    '-10, -9, -8, -7, -6, -5, -4, -3, -2'
    >>> calcular_numeros_no_intervalo(-1, -10)
    ''

"""


def calcular_numeros_no_intervalo(inicio: int, fim: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    try: 
        lista = ''
        start = inicio
        end = fim
        tamanho = len(range(start,end))
    
        for num in range(start, end):
            tamanho -= 1
            if tamanho == 0:
                lista += str(num)
            else:
                lista += str(num) + ', '
                 
    except ValueError:
        print('Entrada inválida!!!')
    
    return print(f"'{lista}'")

#calcular_numeros_no_intervalo(1, 10)