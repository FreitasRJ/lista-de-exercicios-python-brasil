"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> vogal_ou_consoante("F")
    'consoante'
    >>> vogal_ou_consoante("a")
    'vogal'
    >>> vogal_ou_consoante('c')
    'consoante'
    >>> vogal_ou_consoante('U')
    'vogal'
"""




def vogal_ou_consoante(letra):
    """Escreva aqui em baixo a sua solução"""
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']

    #letra = input("Digite uma letra: ").lower()    
    letra = letra.lower() 

    if letra in vogais:
        resposta = "'vogal'"
            
    elif letra in consoantes:
        resposta = "'consoante'"
    return print(resposta)        
    
#vogal_ou_consoante('F')