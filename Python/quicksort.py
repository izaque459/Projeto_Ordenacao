#data:01/01/2025
# o famoso algorimto quicksort eh o algoritmo que uma vez bem 
# implementado pode se tornar o favorito em ordenacoes
from palavras import palavras
import random

def choosepivotrandom(l,r):
    # escolha aleatorio de um pivo eh combinacao de escolher
    # entre o primeiro elemento ou outro qualquer proximo da mediana
    return random.randint(l,r)

def quicksort(input_list):
    
    def choosepivot(input_list,l,r):
    
        return choosepivotrandom(l,r)

    def partition(input_list,l,r):
        p = input_list[l]
        i = l + 1
        aux = 0
        for j in range(l+1,r)
            if input_list[j] < p :
                aux = input_list[j]
                input_list[j] = input_list[i]
                input_list[i] = aux
                i += 1
            aux = input_list[l]
            input_list[l] = input_list[i-1]
            input_list[i-1] = aux
        
        return i - 1
    
    def orders(input_list,l,r):
        
        if l >= r: 
            return None
        
        pivot = choosepivot(input_list,l,r)
        
        aux = input_list[pivot]
        input_list[pivot] = input_list[l]
        input_list[l] = aux

        new_pivot = partition(input_list,l,r)
        
        orders(input_list,l,new_pivot-1)
        orders(input_list,new_pivot+1,r)

    orders(input_list,0,len(input_list)-1)