# Data: 06/01/2025
# O metodo ShellSort eh uma extensão do metodo InsertionSort
# A implementacao é uma versao de outra implementacao usando goto 
from palavras import palavras

def shellsort(input_list):

    h = 1
    n = len(input_list)
    
    while True:             # repita
        h = 3*h+1           #   h = 3*h+1    
        if h>n:             # ateh h > n
            break
    
    while True:                                  # repita
    
        
        h = h % 3
        
        for i in range(h+1,n):
            x = input_list[i]
            j = i
             
            while input_list[j-h] > x:
               input_list[j] = input_list[j-h]
               j-=h
               if j<=h :                        #           if j <= h :
                   break                        #               goto Label
        
            input_list[j] = x
                                                # Label
        if h == 1:
            break

print("\n Palavras em ordem qualquer \n")
print(palavras)
shellsort(palavras)
print("\n Palavras ordenadas pelo algoritmo ShellSort \n")
print(palavras)