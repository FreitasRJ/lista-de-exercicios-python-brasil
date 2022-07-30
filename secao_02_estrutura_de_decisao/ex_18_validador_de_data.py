"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e 
determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    def ver_bissexto(ano):
        quatro = ano % 4
        cem = ano % 100
        quatrocentos = ano % 400
                    
        # primeira situação
        if quatro == 0:
            if cem != 0:  
                mensagem = "bissexto"
            else:
                mensagem = "Não é bissexto"
                    
        #segunda situação    
        if quatro != 0:
            if quatrocentos == 0: 
                mensagem = "bissexto"
            else:
                mensagem = "Não é bissexto"
                
        #terceira condição
        if quatro != 0:
            if quatrocentos == 0:
                mensagem = "bissexto"
            else:
                mensagem = "Não é bissexto"
        return mensagem

    
  
        
    aviso = "'Data válida'"
    #data = input('Entre com uma data dd/mm/aaaa: ')
    tam = len(data)
    if tam < 8 or tam > 10:
        aviso ="'Data inválida'"
    
    else:
        data = data.rsplit('/')
        dd = int(data[0])
        mm = int(data[1])
        aaaa = int(data[2])
        
        mensagem = ver_bissexto(aaaa)
                
        if dd < 1:
            aviso = "'Data inválida'"
        elif mm < 1 or mm > 12:
            aviso = "'Data inválida'"
                    
        elif mm == 2 and mensagem != "bissexto" and dd > 28:
            aviso = "'Data inválida'"
                
        elif mm == 2 and mensagem == "bissexto" and dd > 29:
            aviso = "'Data inválida'"     
                
        elif mm % 2 == 0 and mm != 2 and dd > 30:
            aviso = "'Data inválida'"
                    
        elif mm % 2 != 0 and dd >31:
            aviso = "'Data inválida'"
                    
    print(aviso)
      
    
#validar_data('')