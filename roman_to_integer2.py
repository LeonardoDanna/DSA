class Solution: 
    def romanToInt(self, s):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} # Mapeamento dos símbolos romanos para valores utilizando um dicionário.
        
        #largest to smallest: add them up
        #smaller before larger: subtract them
        
        res = 0
        for i in range(len(s)): #percorre o array
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]: #verifica se o próximo símbolo é maior que o atual
                res -= roman_map[s[i]] #subtrai o valor do símbolo atual do resultado
            else:
                res += roman_map[s[i]] #adiciona o valor do símbolo atual ao resultado
        return res