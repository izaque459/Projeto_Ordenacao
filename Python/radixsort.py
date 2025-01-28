from countingsort import gerarlista

def countingsort(arr, exp):
    
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Assume base 10 (0-9)

    for i in range(n):
        index = (arr[i] // exp) % 10  # Extrai o dígito
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output

def radixsort(input_list):
    
    m = max(input_list)
    exp = 1
       
    while m / exp >= 1:
        input_list = countingsort(input_list,exp)
        exp *= 10
        
    return input_list
    
# Exemplo de uso:
tam = 25  # Tamanho da lista a ser gerada
minimo = 0   # Valor mínimo dos números aleatórios
maximo = 1100 # Valor máximo dos números aleatórios

try:
    lista_para_ordenar = gerarlista(tam, minimo, maximo)

    print("Lista não ordenada:", lista_para_ordenar)

    lista_ordenada = radixsort(lista_para_ordenar)
    print("Lista ordenada:", lista_ordenada)

except ValueError as e:
    print(f"Erro: {e}")
   
   
# Teste de corretude 
lista_ordenada_python = sorted(lista_para_ordenar)
if lista_ordenada == lista_ordenada_python:
    print("\nOrdenação correta!")
else:
    print("\nOrdenação INCORRETA!")
        