class Solution:
    def reverseWords(self, s):
        words = s.split(' ')  # Divide a string em palavras
        reversed_words = [word[::-1] for word in words]  # Inverte cada palavra
        return ' '.join(reversed_words)  # Junta as palavras com espaços