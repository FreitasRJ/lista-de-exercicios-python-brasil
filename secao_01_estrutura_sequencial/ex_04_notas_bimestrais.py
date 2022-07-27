"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media():
    """Escreva aqui em baixo a sua solução"""
    while True:
        soma = 0
        try:
            for n in range(1,5):
                notas = float(input(f'Informe a nota do bimestre {n}: '))
                soma += notas 
            print(f'A média anual é {soma / 4}')

            break
        except ValueError:
            print('Não foi digitado um número!!!')
            break

