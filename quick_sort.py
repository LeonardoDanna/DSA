def quicksort(arr): 
    def partition(low, high): # particiona o array em torno de um pivô e retorna o índice do pivô
        pivot = arr[high] # escolhe o último elemento como pivô
        i = low - 1 # índice do menor elemento
        for j in range(low, high):
            if arr[j] <= pivot: # se o elemento atual é menor ou igual ao pivô
                i += 1 # incrementa o índice do menor elemento
                arr[i], arr[j] = arr[j], arr[i] # troca os elementos
        arr[i + 1], arr[high] = arr[high], arr[i + 1] # troca o pivô para a posição correta
        return i + 1 # retorna o índice do pivô

    def quicksort_recursive(low, high):
        if low < high: ## se o subarray tem mais de um elemento
            pi = partition(low, high) # particiona o subarray e obtém o índice do pivô
            quicksort_recursive(low, pi - 1) # ordena o subarray à esquerda do pivô
            quicksort_recursive(pi + 1, high) # ordena o subarray à direita do pivô

    quicksort_recursive(0, len(arr) - 1) # chama a função recursiva para ordenar o array inteiro
    return arr


test_array = [10, 7, 8, 9, 1, 5]
print("Unsorted array:", test_array)
sorted_array = quicksort(test_array)
print("Sorted array:", sorted_array)