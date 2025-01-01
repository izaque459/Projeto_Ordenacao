#data: 01/01/2025
# o algoritmo mergesort é um exemplo classico do algoritmo dividir e conquistar para ordenacao

from palavras import palavras

def mergesort(input_list):
    n = len(input_list)
    
    def merge(left_list,right_list):
        n = len(left_list) + len(right_list)
        i = j = 0
        result = []
        for k in range(n):
            if i == len(left_list):     # Condição para checar se uma lista está vazia
                result.append(right_list[j])  
                j+=1
            elif j == len(right_list):     # Condição para checar se uma lista está vazia
                result.append(left_list[i])  
                i+=1
            elif left_list[i] < right_list[j]:
                result.append(left_list[i])
                i += 1
            else:
                result.append(right_list[j])
                j += 1
          
        return result
            
            
    if n<=1:
        return input_list
        
    middle = n //2
    left_list = mergesort(input_list[:middle])
    right_list = mergesort(input_list[middle:])
    
    result_list = merge(left_list,right_list)
    
    return result_list
    
 
print("\n Palavras em ordem qualquer \n")
print(palavras)
palavras_ordenadas = mergesort(palavras)
print("\n Palavras ordenadas pelo algoritmo MergeSort\ n")
print(palavras_ordenadas)