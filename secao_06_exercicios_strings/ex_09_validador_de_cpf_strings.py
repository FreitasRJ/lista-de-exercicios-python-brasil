"""
Exercício 09 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores
e dos caracteres de formatação.

    >>> validar_cpf('734.289.251-30')
    True


    >>> validar_cpf('732.289.294-10')
    False


    >>> validar_cpf('44986045040')
    True


    >>> validar_cpf('6693171008')
    False


"""


import re

def validar_cpf(cpf):
    """Escreva aqui em baixo a sua solução"""
    # https://www.calculadorafacil.com.br/computacao/validar-cpf

    #if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        #return False
    
    # Confere se são 11 digitos e diferentes
    cpf = [int(digitos) for digitos in cpf if digitos.isdigit()]
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    # identifica o primeiro digito verificador.
    soma_primeiro_peso = sum(digito * peso for digito, peso in zip(cpf, range(1,10)))
    digito_verificador_1 = soma_primeiro_peso % 11
    
    if digito_verificador_1 == 10:
        digito_verificador_1 = 0
    
    # acrescentar o digito verificador aos 9 primeiros numeros do cpf.
    cpf_9_digitos = (cpf[0:9])
    cpf_9_digitos.append(digito_verificador_1)
    
    # identifica o segundo digito verificador.
    soma_segundo_peso = sum(digito * peso for digito, peso in zip(cpf_9_digitos, range(0,10)))
    digito_verificador_2 = soma_segundo_peso % 11

    if digito_verificador_2 == 10:
        digito_verificador_2 = 0
    
    if digito_verificador_1 != cpf[-2] or digito_verificador_2 != cpf[-1]:
        return False
    
    return True




