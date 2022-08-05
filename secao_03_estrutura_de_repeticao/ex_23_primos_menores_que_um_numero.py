"""
Exercício 23 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre todos os primos entre 1 e N sendo N um número 
inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para 
encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) 
executados.

    >>> primos, divisoes = calcular_primos_e_divisoes(0)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(1)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(2)
    >>> primos
    '2'
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(3)
    >>> primos
    '2, 3'
    >>> divisoes <= 1
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(4)
    >>> primos
    '2, 3'
    >>> divisoes <= 3
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(5)
    >>> primos
    '2, 3, 5'
    >>> divisoes <= 6
    True

"""

def calcular_primos_e_divisoes(n: int) -> tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""
    """
    Crivo de Erastóstenes: (elimina os números compostos)
    Ex.:
    n = 10
    * lista com todos os numero de 2(primeiro primo) até n(25)
        2, 3, 4, 5, 6, 7, 8, 9, 10.
    * Excluir dessa lista, todos os multiplos do primeiro primo (2 único primo par)
        (2), 3, X, 5, X, 7, X, 9, X
    * passar para segundo número e excluir seus multiplos.
        2, (3), 5, 7, X
    * seguindo esse procedimento temos os números primos entre 1 e n:
        2, 3, 5 e 7
    """
    divisoes = 0
    saida = ""
    # C = composto e P = primo
    primos=[]
    if n != 0:
        conjunto = ["P"] * (n + 1)
        conjunto[0] = conjunto[1] = "C" 
        for num, tipo in enumerate(conjunto):
            #print(num, tipo, "+++")
            if tipo == "P":
                primos.append(num)
                for idx in range(num **2, n + 1, num):
                    conjunto[idx] = "C"
                    #print(idx)
    for idx in primos:
        saida += str(idx)
    saida = ', '.join(saida)
    saida = f'{saida}'
    
    return [saida, divisoes]

#print(calcular_primos_e_divisoes(10))