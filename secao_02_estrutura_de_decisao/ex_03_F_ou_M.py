"""
Exercício 03 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Retorne: F - Feminino ou M - Masculino. Para quaisquer outros valores, retorne Sexo Inválido.

    >>> f_ou_m("F")
    'F - Feminino'
    >>> f_ou_m("M")
    'M - Masculino'
    >>> f_ou_m('Z')
    'Sexo inválido'
    >>> f_ou_m(1)
    'Sexo inválido'
"""


def f_ou_m(sexo):
    """Escreva aqui em baixo a sua solução"""
    #sexo = input('Digite: (F) - Feminino ou  (M) - Masculino:  ')
    
    if sexo in  ['f','F']:
        mensagem ="'F - Feminino'"
    elif sexo in  ['m', 'M']:
        mensagem = "'M - Masculino'"   
    else:
        mensagem = "'Sexo inválido'"
        
    print(mensagem)

#f_ou_m('f')