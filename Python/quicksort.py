#data:01/01/2025
# o famoso algorimto quicksort eh o algoritmo que uma vez bem 
# implementado pode se tornar o favorito em ordenacoes
from palavras import palavras
import random

def indexpivot(input_list,l,r):
    # escolha aleatorio de um pivo eh combinacao de escolher
    # entre o primeiro elemento ou outro qualquer proximo da mediana
    return random.randint(l,r)

def partition(input_list,l,r): 
        i = l
        j = r
        pivot = input_list[indexpivot(input_list,l,r)]
        
        while True:
            while input_list[i] < pivot:
                i+=1
            while input_list[j] > pivot:
                j-=1
            if i <= j:
                input_list[i], input_list[j] = input_list[j], input_list[i]
                i+=1
                j-=1
            if i > j:
                break
        
        return i,j
    
def orders(input_list,l,r): 
    
    i,j = partition(input_list,l,r)
    
    if l < j:
        orders(input_list,l,j)
    if i < r:
        orders(input_list,i,r)
            

def quicksort(input_list):

    orders(input_list,0,len(input_list)-1) 
   
    
print("\n Palavras em ordem qualquer \n")
print(palavras)
quicksort(palavras)
print("\n Palavras ordenadas pelo algoritmo QuickSort \n")
print(palavras)