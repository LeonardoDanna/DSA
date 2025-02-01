class Solution(object):
    def isValid(self, s):
        stack = [] 
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"} #cria um dicionario com os pares de parenteses

        for c in s: #percorre a string
            if c in closeToOpen: #se o caracter está no dicionario
                if stack and stack[-1] == closeToOpen[c]: #se o ultimo elemento da pilha é igual ao valor do dicionario
                    stack.pop() #remove o ultimo elemento da pilha
                else:
                    return False
            else:
                stack.append(c) #adiciona o caracter na pilha
        return True if not stack else False #se a pilha está vazia, retorna True, caso contrario, retorna False