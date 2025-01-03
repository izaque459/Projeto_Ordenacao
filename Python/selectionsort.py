# Data: 03/01/2025
# Implementação do algoritmo da ordenação por seleção
from palavras import palavras

def selectionsort(input_list):
    Min = None
    n = len(input_list)
    for i in range(n-1):
        Min = i
        for j in range(i+1,n):
            if input_list[j] < input_list[Min]:
                Min = j
        input_list[Min], input_list[i] = input_list[i], input_list[Min]



print("\n Palavras em ordem qualquer \n")
print(palavras)
selectionsort(palavras)
print("\n Palavras ordenadas pelo algoritmo SelectionSort \n")
print(palavras)