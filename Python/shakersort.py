from palavras import palavras
# Data: 06/01/2025
# O metodo SkakerSort é uma variação do metodo BubbleSort 
# Cada iteração ocorre nas dois sentidos do array

def shakersort(input_list):
    n = len(input_list)
    l = 0  # Índice inicial da esquerda
    r = n - 1  # Índice inicial da direita
    k = 0

    while l < r:
        for j in range(l, r):  # Itera da esquerda para a direita
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                k = j + 1 # k recebe o valor do indice do ultimo swap

        r = k #atualiza o indice da direita com o ultimo indice do swap
        if l >= r:
            break

        for j in range(r, l, -1):  # Itera da direita para a esquerda
            if input_list[j] < input_list[j - 1]:
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
                k = j - 1 # k recebe o valor do indice do ultimo swap
                
        l = k #atualiza o indice da esquerda com o ultimo indice do swap
        if l >= r:
            break

print("\n Palavras em ordem qualquer \n")
print(palavras)
shakersort(palavras)
print("\n Palavras ordenadas pelo algoritmo ShakerSort \n")
print(palavras)