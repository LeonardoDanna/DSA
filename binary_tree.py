class Solution(object):
    def maxDepth(self, root):
        if not root: # se a raiz é nula, retorna 0
            return 0 # se não, retorna o máximo entre a profundidade da esquerda e a profundidade da direita

        def dfs(root, depth): # função recursiva que retorna a profundidade da árvore
            if not root: return depth # se a raiz é nula, retorna a profundidade

            return max(dfs(root.left, depth+1), dfs(root.right, depth+1)) # retorna o máximo entre a profundidade da esquerda e a profundidade da direita

        return dfs(root, 0) # retorna a profundidade da árvore