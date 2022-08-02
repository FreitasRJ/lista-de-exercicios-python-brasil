"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
n−ésimo termo.

    >>> calcular_serie_de_fibonacci(1)
    '1'
    >>> calcular_serie_de_fibonacci(2)
    '1, 1'
    >>> calcular_serie_de_fibonacci(3)
    '1, 1, 2'
    >>> calcular_serie_de_fibonacci(4)
    '1, 1, 2, 3'
    >>> calcular_serie_de_fibonacci(5)
    '1, 1, 2, 3, 5'
    >>> calcular_serie_de_fibonacci(6)
    '1, 1, 2, 3, 5, 8'
    >>> calcular_serie_de_fibonacci(7)
    '1, 1, 2, 3, 5, 8, 13'

"""


def calcular_serie_de_fibonacci(n: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    primeiro = 0
    segundo = 1
    conta = 0
    fibona = ''
    
    try:
        #n = int(input('Fibonacci. Entre o número de temos: '))
    
        while conta <= (n-2):
            terceiro = primeiro + segundo
            fibona += f", {terceiro}"
            primeiro = segundo
            segundo = terceiro      
            conta += 1

        print(f"'1{fibona}'")

    except ValueError:
        print('Entrada inválida!!!')

#calcular_serie_de_fibonacci(7)

  