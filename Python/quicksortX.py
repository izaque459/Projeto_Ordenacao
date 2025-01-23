#data:23/01/2025
# o famoso algoritmo quicksortX otimizado para evitar seu pior caso
# implementado corretamente pode se tornar o favorito em ordenacoes
from palavras import palavras
import random

def indexpivot(input_list,l,r):
    # escolha aleatoriamente três elementos da lista
    # para retornar o indice da mediana desses três
    
    #    if (input_list[i] < input_list[j] and input_list[j] < input_list[k]) or (input_list[k] < input_list[j] and input_list[j] < input_list[i]):
    #        return  j
    #    elif (input_list[j] < input_list[i] and input_list[i]< input_list[k]) or (input_list[k] < input_list[i] and input_list[i]< input_list[j]):
    #        return i
    #    else:
    #        return k

    i = random.randint(l,r)
    j = random.randint(l,r)
    k = random.randint(l,r)
    
    a = input_list[i]
    b = input_list[j]
    c = input_list[k]

    if (a <= b <= c) or (c <= b <= a):
        return j
    elif (b <= a <= c) or (c <= a <= b):
        return i
    else:
        return k
    
def insertionsortX(input_list,l,r):
    x = None                
    j = 0                                   
    
    for i in range(l+1,r+1):                  
        x = input_list[i]
        j = i - 1
                                                
        while j>=0 and x < input_list[j]:       
            input_list[j+1] = input_list[j]
            j -= 1
        input_list[j+1] = x



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
    
    if (r - l +1) <=20:
        insertionsortX(input_list,l,r)
    else:
        if l < j:
            orders(input_list,l,j)
        if i < r:
            orders(input_list,i,r)
            

def quicksortX(input_list):

    orders(input_list,0,len(input_list)-1) 
   
    

teste = sorted(palavras)

print("\n Palavras em ordem qualquer \n")
print(palavras)
quicksortX(palavras)
print("\n Palavras ordenadas pelo algoritmo QuickSort X \n")
print(palavras)

if palavras == teste:
    print(" \nPalavras ordenadas corretamente\n")
else:
    print(" \n Palavras ordenadas incorretamente \n")