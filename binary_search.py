def binary_search(nums, n): #recebe um array de numeros e um numero que ele quer encontrar
    lo = 0 #low
    hi = len(nums) #high
    steps = 0
    
    while lo < hi:
        steps +=1
        mid = (lo + hi) // 2 #midpoint
        if nums[mid] == n:
            print("passos: ", steps)
            return mid
        elif nums[mid] < n:
            lo = mid + 1
        else:
            hi = mid
    return -1

#nums = [1, 3, 5, 7, 9, 11, 13, 15]
#n = 7

#result = binary_search(nums, n)
#print("Índice encontrado:", result)