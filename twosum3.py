class Solution(object):
    def twoSum(self, nums, target):
        h = {}  # Cria um dicionário para armazenar os números e seus respectivos índices.

        # Primeiro loop: armazena cada número no dicionário como chave e seu índice como valor.
        for i in range(len(nums)):
            h[nums[i]] = i

        # Segundo loop: verifica se existe um complemento (target - nums[i]) no dicionário.
        for i in range(len(nums)):
            y = target - nums[i]  # Calcula o complemento necessário para atingir o alvo.

            # Se o complemento existir no dicionário e não for o mesmo índice do número atual, retorna os índices.
            if y in h and h[y] != i:
                return [i, h[y]]  # Retorna a posição dos dois números que somam o alvo.
