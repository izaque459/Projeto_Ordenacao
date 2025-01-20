#data 20/01/2025
# Metodo bubblesort é considerado um metodo infame, pois seu tempo de ordenacao é quadratico

from palavras import palavras

def bubblesort(input_list):

    tam = len(input_list)
    for i in range(tam-1):
        for j in range(tam-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
   


teste = sorted(palavras)

print("\n Palavras em ordem qualquer \n")
print(palavras)
bubblesort(palavras)
print("\n Palavras ordenadas pelo algoritmo BubbleSort \n")
print(palavras)

if palavras == teste:
    print(" \nPalavras ordenadas corretamente\n")
else:
    print(" \n Palavras ordenadas incorretamente \n")