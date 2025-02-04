class Solution(object):
    def moveZeroes(self, nums):
        pos = 0 #cria um ponteiro no indice 0

        for i in range(len(nums)): #percorre o array
            if nums[i] != 0: #se o numero da vez for diferente de zero
                nums[pos], nums[i] = nums[i], nums[pos] # troca o numero da posição pos com o numero da posição atual
                pos += 1 #incrementa o ponteiro
        