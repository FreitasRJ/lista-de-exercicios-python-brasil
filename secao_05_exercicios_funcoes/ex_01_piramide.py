"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Faça um programa para imprimir:

  1
  2   2
  3   3   3
  .....
  n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

"""
n = 3
#n = int(input('Digite um número: '))
for linha in range(n+1):
    lin = str(linha)
    saida = ''
    for n in range(linha):
        saida = saida + lin + '  '
    print(saida)