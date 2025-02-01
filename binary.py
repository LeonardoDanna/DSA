class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += n & 1 #comparacao bit a bit com 1 e soma o resultado na variavel res
            n = n >> 1 #desloca n para a direita em 1 bit

        return res