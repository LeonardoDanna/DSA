class Solution(object):
    def longestCommonPrefix(self, s):
        for i in range(len(s)): #percorre o array
            if len(s) == 0: #verifica se o array está vazio
                return "" 
            prefix = s[0] #define o prefixo como o primeiro elemento do array
            for i in range(1,len(s)): #percorre o array a partir do segundo elemento
                while s[i].find(prefix) != 0: #verifica se o prefixo está no elemento atual
                    prefix = prefix[0 : len(prefix) - 1] #remove o último caractere do prefixo
                    if prefix == "": #verifica se o prefixo está vazio
                        return "" 
            return prefix