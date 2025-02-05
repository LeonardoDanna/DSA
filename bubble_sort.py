def bubble_sort(arr): 
    n = len(arr) # Obtém o tamanho do array
    for i in range(n): # Loop externo para controlar o número de iterações
        for j in range(0, n - i - 1): # Loop interno para comparar e trocar elementos
            if arr[j] > arr[j + 1]: # Verifica se o elemento atual é maior que o próximo
                is_sorted = True # Define que a lista ainda não está ordenada
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Troca os elementos
        if is_sorted: # Se a lista já estiver ordenada, interrompe o loop
            return # Retorna a lista ordenada
        
bubble_sort([1, 3, 2, 5, 4])