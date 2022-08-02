"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    tam = len(numeros)
    soma = 0
    mensagem = "'Maior valor: não existe. Menor valor: não existe. Soma: 0'"
    if tam != 0:
        if tam == 1:
            maior = menor = soma = numeros[0]
            mensagem = f"'Maior valor: {numeros[0]}. Menor valor: {numeros[0]}. Soma: {numeros[0]}'"
        else:
            for idx in range(tam):
                soma += numeros[idx]
                if not (0 <= numeros[idx] <= 1000):
                    mensagem = "'Somente números de 0 a 1000 são permitidos'"
                else:  
                    maior = numeros[0]
                    menor = numeros[1]
                    for indx in range(tam):
                        
                        if maior < numeros[indx]:
                            maior = numeros[indx]
                        if menor > numeros[indx]:
                            menor = numeros[indx] 
                    mensagem = f"'Maior valor: {maior}. Menor valor: {menor}. Soma: {soma}'"
      
    print(mensagem)
