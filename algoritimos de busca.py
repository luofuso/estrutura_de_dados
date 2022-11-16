import numpy
class MyArrayList:
 def __init__(self, maxsize):
    self.items = numpy.zeros((maxsize,), dtype=int)
    self.count = 0
 def AddLast(self, newItem):
    if (self.IsFull()):
        raise Exception("lista cheia")
    self.items[self.count] = newItem
    self.count += 1
 def IsFull(self):
    return self.count == len(self.items)

def LinearSeach_SortedArray(self, key):
    n=len(self.items)
    k = 0
    while (k<n and self.items[k]<key):
        k+=1
    if (k<n and self.items[k] == key):
        return(True)
    else:
        return(False)

def BinarySearch(self,key):
    min = 0
    max = len(self) - 1
    while (min<=max):
        mid = (min+max)//2
    if (key == self.items[mid]):
        return (True)
    elif (key < self.items[mid]):
        max= mid-1
    else:
        min = mid +1

n = 1000
max = 100000
lista = MyArrayList(n)
import random

contador = 0
print("Preenchendo o array com os elementos aleatórios...")
while contador < n :
    x = random.randint(0,max)
    lista.AddLast(x)
    contador+=1

def SortList(self):
    self.items.sort()

SortList(lista)
print("Ordenando...")
contador=0
print("Efetuando 200 buscas...")
import datetime
start= datetime.datetime.now()
while contador < 2*max:
    contador+=1
    x = random.randint(0,2*max)
    BinarySearch(x)

end= datetime.datetime.now()
delta=end-start
print("Tempo gasto nas buscas:", delta)
