"""
Exercício 21 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é
divisível somente por ele mesmo e por 1.

    >>> eh_primo(0)
    False
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    False
    >>> eh_primo(5)
    True
    >>> eh_primo(6)
    False
    >>> eh_primo(7)
    True
    >>> eh_primo(8)
    False
    >>> eh_primo(9)
    False
    >>> eh_primo(10)
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(547)
    True
    >>> eh_primo(548)
    False

"""


def eh_primo(n: int) -> bool:
    """Escreva aqui em baixo a sua solução"""
    resposta = ""
    try:
        #n = int(input("Digite um número inteiro: "))
        if n < 2:
            resposta = False
        if n == 2:
            resposta = True
        if n > 2:
            resposta = True
            result = cont = 1
            while result !=0 and cont < n:
                result = n % cont
                if result == 0:
                    resposta = False
                cont +=1

        print(resposta)
              
    except ValueError:
        print('Entrada inválida!!!')
#eh_primo(2)