"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""

import operator
import statistics

def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    cid_lista = []
    cid = ""
    car = 0
    carros_m_15k = 0
    quant = 0
    for idx in range(len(cidades)):
        acidentes = (cidades[idx][2]/cidades[idx][1])*1000
        cid = (cidades[idx][0], cidades[idx][1], cidades[idx][2], acidentes)
        car += cidades[idx][1]

        if cidades[idx][1] <= 150_000:
            carros_m_15k += cidades[idx][2]
            quant +=1
        
        cid_lista.append(cid)
        
    cidade_m, carros, acidentes, maior_ind_acidentes = max(cid_lista,key=operator.itemgetter(3))
    cidade_menor, carros, acidentes, menor_ind_acidentes = min(cid_lista,key=operator.itemgetter(3))
    media_veic_m = carros_m_15k / quant
    media_veic = car/(len(cidades))
    
    print(f'O maior índice de acidentes é de {cidade_m}, com {maior_ind_acidentes:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {cidade_menor}, com {menor_ind_acidentes:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {media_veic:.0f}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_veic_m} acidentes.')

#calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    # ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900))

