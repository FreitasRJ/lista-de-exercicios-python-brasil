"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao


Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido.
Também mostre a soma dos números da sequência.

    >>> calcular_numeros_no_intervalo_e_somar(1, 10)
    'Sequência: 1, 2, 3, 4, 5, 6, 7, 8, 9. Soma: 45'
    >>> calcular_numeros_no_intervalo_e_somar(-10, -1)
    'Sequência: -10, -9, -8, -7, -6, -5, -4, -3, -2. Soma: -54'
    >>> calcular_numeros_no_intervalo_e_somar(-1, -10)
    'Sequência: vazia. Soma: 0'

"""


def calcular_numeros_no_intervalo_e_somar(inicio: int, fim: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    start = inicio
    end = fim
    try:
                    
        #start = int(input('Entre com o primeiro número inteiro: '))
        #end = int(input('Entre com o segundo número inteiro: '))
        numero = start
        contador = inicio
        soma = 0
        mensagem = ""
        while  start <= contador < end:

            contador += 1
            soma += numero
            mensagem += str(numero)
            if numero < end-1:
                mensagem += ', '
            numero += 1 
        if soma == 0:
            mensagem = "vazia" 
        print(f"'Sequência: {mensagem}. Soma: {soma}'")
    except ValueError:
        print('Entrada inválida!!!')  
#calcular_numeros_no_intervalo_e_somar(-1, -10)