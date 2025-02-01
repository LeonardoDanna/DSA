phone_keyboard = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

class Solution(object):
    def letterCombinations(self, digits):
        if not digits: return [] #se a string está vazia, retorna uma lista vazia

        res = [] 
        def bt(permutation, digits): #função recursiva que gera as combinações
            if not digits:
                res.append(permutation) #adiciona a combinação na lista
                return
            # A
            for letter in phone_keyboard[digits[0]]: #percorre a lista de letras do dicionario
                bt(permutation+letter, digits[1:]) #chama a função recursivamente
                # D E F

        bt("", digits) #chama a função recursivamente
        return res