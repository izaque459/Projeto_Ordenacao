# data:02/01/2025
# Implementacao do algoritmo ordenção por insercao 

from palavras import palavras


def insertionsort(input_list):
    x = None
    tam = len(input_list)                  # Com uso de sentinela mostrado na linha 15
    j = 0                                   # e demais alterações necessarias
    
    for i in range(1,tam):                  #for i in range(2,tam):
        x = input_list[i]
        j = i - 1
                                                #input_list[0] = x 
        while j>=0 and x < input_list[j]:       #while x < input_list[j]:
            input_list[j+1] = input_list[j]
            j -= 1
        input_list[j+1] = x
        
print("\n Palavras em ordem qualquer \n")
print(palavras)
insertionsort(palavras)
print("\n Palavras ordenadas pelo algoritmo InsertionSort \n")
print(palavras)