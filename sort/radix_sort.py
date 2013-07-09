#
#author github @nicolasmancera  
from random import uniform 
def radixsort(lista): 
    cifras=contar(lista) 
    mod=10 
    div=1 
    for i in range(0, cifras): 
        lista=ponerCola(lista, mod, div) 
        mod*=10 
        div*=10 
    return lista 
 
def contar(lista): 
    max=mayor(lista) 
    largo=0 
    while ((max/10)!=0) : 
      max=int(max/10) 
      largo+=1 
    return largo 
 
def mayor(lista) : 
  max=0 
  for i in range(0,len(lista)) : 
    if (max<lista[i]) : 
      max=lista[i] 
    return max 
 
def ponerCola(lista, mod, div): 
    colas = [ [], [], [], [], [], [], [], [], [], [] ] 
    temp = [] 
    for i in range(0, len(lista)): 
        colas[lista[i] % mod / div].append(lista[i]) 
    for i in range(0, 10): 
        temp.extend(colas[i]) 
    return temp
