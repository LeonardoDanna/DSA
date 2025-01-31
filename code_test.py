def solution(Array):
    N = len(Array) #tamanho do array
    nums = set() #cria um conjunto para armazenar os números
    
    for num in Array: #vai percorrendo o array
        if 1 <= num <= N: #se o número for maior que 1 e menor que o tamanho do array
            nums.add(num)  # adiciona o número no conjunto
    
    for i in range(1, N + 2):  #percorre os números de 1 até N + 1
        if i not in nums: #se o número não está no conjunto
            return i #retorna o número que está faltando
