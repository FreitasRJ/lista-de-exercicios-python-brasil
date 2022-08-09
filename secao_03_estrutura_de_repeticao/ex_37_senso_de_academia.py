"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""
import statistics
def rodar_senso():
    """Escreva aqui em baixo a sua solução"""   
    nomes = []
    alturas = []
    pesos = []
    
    try:
        while True:
            
            nome = input('Digite o nome: ')
            if nome != '0':
                nomes.append(nome)
                altura = int(input('Digite a altura em centimetro: '))
                alturas.append(altura)
                peso = int(input('Digite o peso em kg: '))
                pesos.append(peso)

            else:
                mais_alto = max(alturas)
                mais_baixo = min(alturas)
                mais_gordo = max(pesos)
                mais_magro = min(pesos)
                for idx in range(len(nomes)):
                    if alturas[idx] == mais_alto:
                        nome_mais_alto = nomes[idx]
                    if alturas[idx] == mais_baixo:
                        nome_mais_baixo = nomes[idx] 
                    if pesos[idx] == mais_magro:
                        nome_mais_magro = nomes[idx]    
                    if pesos[idx] == mais_gordo:
                        nome_mais_gordo = nomes[idx]
                media_alturas = statistics.mean(alturas)
                media_pesos = statistics.mean(pesos)
                
                print(f'Cliente mais alto: {nome_mais_alto}, com {mais_alto} centímetros')
                print(f'Cliente mais baixo: {nome_mais_baixo}, com {mais_baixo} centímetros')
                print(f'Cliente mais magro: {nome_mais_magro}, com {mais_magro} kilos')
                print(f'Cliente mais gordo: {nome_mais_gordo}, com {mais_gordo} kilos')
                print('--------------------------------------------------')
                print(f'Media de altura dos clientes: {media_alturas:.1f} centímetros')
                print(f'Media de peso dos clientes: {media_pesos:.1f} kilos')
                break
    except ValueError:
        print('Entrada inválida!!!')
#rodar_senso()
# Outra solução seria utilizar operator.itemgetter(n).



