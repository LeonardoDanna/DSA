class Solution(object):
    def twoSum(self, nums, target): 
        h = {} #cria um dicionário vazio

        for i in range(len(nums)): #percorre o array
            h[nums[i]] = i #adiciona o número como chave e o índice como valor

        for i in range(len(nums)): #percorre o array
            y = target - nums[i] # calcula o complemento

            if y in h and h[y] != i: #verifica se o complemento está no dicionário e se o índice é diferente do índice do número atual
                return[i, h[y]] # retorna os índices dos números que somam o alvo