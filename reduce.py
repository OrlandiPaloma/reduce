'''
recebe uma lista e retorna um único valor desta lista.
Por exemplo, retorna a soma dos valores de uma lista.
lista = [1,3,5,10,20]
Reduce vai retornar o número 39, que corresponde à soma total.
'''

from functools import reduce

def soma(x,y):
  return x+y
  
lista=[1,3,5,10,20]

soma_lista = reduce(soma, lista)
print(soma_lista)
