class Solution(object):
    def reverseList(self, head):
        # Inicializa a nova lista como None (será a cabeça da lista invertida)
        new_list = None  

        # Percorre a lista original
        while head:
            # Armazena o próximo nó antes de alterar as referências
            next_node = head.next  
            
            # Inverte a direção do ponteiro do nó atual
            head.next = new_list  
            
            # Move o novo cabeçalho para o nó atual
            new_list = head  
            
            # Avança para o próximo nó da lista original
            head = next_node  
        
        # Retorna o novo cabeçalho da lista invertida
        return new_list  
