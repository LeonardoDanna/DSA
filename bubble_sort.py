def bubble_sort(arr): 
    n = len(arr) # Obtém o tamanho do array
    for i in range(n): # Loop externo para controlar o número de iterações
        for j in range(0, n - i - 1): # Loop interno para comparar e trocar elementos
            if arr[j] > arr[j + 1]: # Verifica se o elemento atual é maior que o próximo
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Troca os elementos