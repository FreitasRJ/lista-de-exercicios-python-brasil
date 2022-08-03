"""
Exercício 22 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa de cálculo dos números primos, informando, caso o 
número não seja primo, por quais número ele é
divisível.
    >>> eh_primo(0)
    False
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    É divisível por 2
    False
    >>> eh_primo(5)
    True
    >>> eh_primo(6)
    É divisível por 2
    É divisível por 3
    False
    >>> eh_primo(7)
    True
    >>> eh_primo(8)
    É divisível por 2
    É divisível por 4
    False
    >>> eh_primo(9)
    É divisível por 3
    False
    >>> eh_primo(10)
    É divisível por 2
    É divisível por 5
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(12)
    É divisível por 2
    É divisível por 3
    É divisível por 4
    É divisível por 6
    False
    >>> eh_primo(547)
    True

"""


def eh_primo(n: int) -> bool:
    """Escreva aqui em baixo a sua solução"""

    if n < 2:
        resposta = False
    if n == 2:
        resposta = True
    if n > 2:
        resposta = True
        result = cont = 1

        while result !=0 and cont < n-1:
            cont +=1   
            result = n % cont
            
            if result != 0:
                resposta = True
            else:
                resposta = False

    if resposta == False:
        for idx in range(2,n):
            if n % idx == 0:
                print(f'É divisível por {idx}')

    print(resposta)

#eh_primo(44)
