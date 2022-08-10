"""
Exercício 42 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-1, 10, 15, 20, 50, 13, 78, 22, 14, 16]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    7 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[14, -5, 10, 2, 80, 99]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    2 número(s) entre o intervalo de zero a 25
    2 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-55, 144, 5, 32, 18, 43, 12, 26, 76]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    3 número(s) entre o intervalo de zero a 25
    3 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[3, 5, 100, -5, 70, 88, 28, 12]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    1 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 51 a 75
    1 número(s) entre o intervalo de 76 a 100

"""


def listar_numeros_para_avaliacao():
    """Escreva aqui em baixo a sua solução"""
    numeros = []
    inter_0_25 = 0
    inter_26_50 = 0
    inter_51_75 = 0
    inter_76_100 = 0

    try:
        while True:
            
            num = int(input('Digite um numero positivo: '))
            if num >= 0:
                numeros.append(num)
            else:
                tam = len(numeros)
                inter_0_25 = [x for x in numeros if x > 0 and x <= 25]
                a = len(inter_0_25)
                inter_26_50 = [x for x in numeros if x > 25 and x <= 50]
                b = len(inter_26_50)
                inter_51_75 = [x for x in numeros if x > 50 and x <= 75]
                c = len(inter_51_75)
                inter_76_100 = [x for x in numeros if x > 75 and x <= 100]
                d = len(inter_76_100)
                
                if a > 0:
                    print(f'{a} número(s) entre o intervalo de zero a 25')
                if b > 0:    
                    print(f'{b} número(s) entre o intervalo de 26 a 50')
                if c > 0:                    
                    print(f'{c} número(s) entre o intervalo de 51 a 75')
                if d > 0:    
                    print(f'{d} número(s) entre o intervalo de 76 a 100')
                break
            
    except ValueError:
        print('Entrada inválida!!!')
#listar_numeros_para_avaliacao()

