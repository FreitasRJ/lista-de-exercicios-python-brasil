"""
Exercício 13 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule e MOSTRE A MÉDIA ANUAL das temperaturas e MOSTRE TODAS AS TEMPERATURAS ACIMA
 DA MÉDIA ANUAL, e em que mês elas ocorreram 
 (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

-as temperaturas só serão dadas em inteiro
-todos os meses do ano serão passados à funçao, começando de janeiro e terminando em dezembro.
 Todos seguidos de sua temperatura mensal

(Funçoês recomendadas para estudo:
    - .ljust()
    - enumerate()
    - sum()
    - len()


    >>> from secao_04_exercicios_lista import ex_13_media_de_temperaturas_anual

    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '30']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 24.75 Graus
     1 - Janeiro:       30°
     2 - Fevereiro:     33°
     3 - Março:         27°
     4 - Abril:         25°
     5 - Maio:          29°
     6 - Junho:         25°
    11 - Novembro:      33°
    12 - Dezembro:      25°
    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '35']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 25.17 Graus
     1 - Janeiro:       35°
     2 - Fevereiro:     33°
     3 - Março:         27°
     5 - Maio:          29°
    11 - Novembro:      33°

"""
#from statistics import mean
import statistics
def temperaturas_acima_da_media():
    """Escreva aqui sua solução: """
    temperaturas = []
    temperaturas_acima = []
    ordem_mes = 0
    meses = 'Janeiro:', 'Fevereiro:', 'Março:', 'Abril:', 'Maio:', 'Junho:', 'Julho:', 'Agosto:', 'Setembro:', 'Outubro:', 'Novembro:', 'Dezembro:'
    for mes in meses:
        temper = int(input(f'Informe a temperatura registrada no mes de {mes}: '))
        temperaturas.append(temper)
        
    media_temperaturas = statistics.mean(temperaturas)
    print(f'Média anual: {media_temperaturas:.2f} Graus')

    for temp in temperaturas:
        #temp = int(temp)
        if temp > media_temperaturas:
            temperaturas_acima.append(f'{ordem_mes + 1:2d} - {meses[ordem_mes]:<14s} {temp:2d}°')
        ordem_mes += 1
        
    for idx in range(len(temperaturas_acima)):
        print(temperaturas_acima[idx])

    return
  
