class Solution: 
    def romanToInt(self, s):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} # Mapeamento dos símbolos romanos para valores utilizando um dicionário.
        
        total = 0
        prev_value = 0
        
        # Iterando de trás para frente
        for i in reversed(s):
            curr_value = roman_map[i]
            
            # Se o valor atual for menor que o anterior, subtraímos, caso contrário, somamos
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            
            prev_value = curr_value
        
        return total
