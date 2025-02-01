class Solution(object):
    def mergeTwoLists(self, list1, list2):
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        dummy = ListNode(-1) # cria um novo nó inicial ficticio 
        current = dummy # aponta o ponteiro current para o nó inicial ficticio

        while list1 and list2: # enquanto as duas listas não estão vazias
            if list1.val < list2.val: # se o valor do nó da lista1 é menor que o valor do nó da lista2
                current.next = list1 # o ponteiro current aponta para o nó da lista1
                list1 = list1.next # o ponteiro list1 aponta para o próximo nó da lista1
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1: # aqui é quando acaba uma das duas listas, então o ponteiro current aponta para o restante da lista que não acabou
            current.next = list1
        else:
            current.next = list2

        return dummy.next # retorna o nó inicial ficticio