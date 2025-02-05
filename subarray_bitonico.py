def longest_bitonic_subarray(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # Arrays auxiliares
    inc = [1] * n
    dec = [1] * n

    # Preenche o array inc[]
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc[i] = inc[i - 1] + 1

    # Preenche o array dec[]
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            dec[i] = dec[i + 1] + 1

    # Calcula o tamanho máximo do subarray bitônico
    max_length = 0
    for i in range(n):
        max_length = max(max_length, inc[i] + dec[i] - 1)

    return max_length

# Exemplo de uso:
arr = [12, 4, 78, 90, 45, 23]
print(longest_bitonic_subarray(arr))  # Saída esperada: 5 (4, 78, 90, 45, 23)
