class Solution:
    def reverseWords(self, s):
        res = ''  # String que armazenará o resultado final
        l, r = 0, 0  # Ponteiros para rastrear o início (l) e o fim (r) de cada palavra

        while r < len(s):  # Loop para percorrer a string
            if s[r] != ' ':  # Se o caractere atual não for um espaço
                r += 1  # Avança o ponteiro da direita (r)
            else:  # Se encontrar um espaço (fim de uma palavra)
                res += s[l:r+1][::-1]  # Inverte a palavra e adiciona ao resultado
                r += 1  # Avança o ponteiro da direita para o próximo caractere
                l = r  # Atualiza o ponteiro da esquerda (l) para o início da próxima palavra

        res += ' '  # Adiciona um espaço ao final do resultado
        res += s[l:r + 2][::-1]  # Inverte a última palavra e adiciona ao resultado
        return res[1:]  # Retorna o resultado, excluindo o espaço inicial

        #s[l:r+1] extrai a palavra, e [::-1] inverte a string.