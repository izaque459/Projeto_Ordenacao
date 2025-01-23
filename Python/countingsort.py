#data:23/01/2025
#o metodo countingsort ordena sem utilizar comparacao A[i]>A[j]
#usado com numeros inteiros e caracteres codificados em valor ascii

import random

def countingsort(arr):
   
    if not arr:  # Verifica se a lista está vazia
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, range_val):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):  # Loop reverso para garantir estabilidade
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output

def gerarlista(tamanho, minimo, maximo):
    
    if minimo > maximo:
        raise ValueError("O valor mínimo deve ser menor ou igual ao valor máximo.")

    lista = [random.randint(minimo, maximo) for _ in range(tamanho)]
    return lista

# Exemplo de uso:
tam = 25  # Tamanho da lista a ser gerada
minimo = 0   # Valor mínimo dos números aleatórios
maximo = 110 # Valor máximo dos números aleatórios

try:
    lista_para_ordenar = gerarlista(tam, minimo, maximo)

    print("Lista não ordenada:", lista_para_ordenar)

    lista_ordenada = countingsort(lista_para_ordenar)
    print("Lista ordenada:", lista_ordenada)

except ValueError as e:
    print(f"Erro: {e}")

# Teste de corretude 
lista_ordenada_python = sorted(lista_para_ordenar)
if lista_ordenada == lista_ordenada_python:
    print("\nOrdenação correta!")
else:
    print("\nOrdenação INCORRETA!")