# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        ahead = head # Inicializa o ponteiro 'ahead' com a cabeça da lista

        while ahead and ahead.next: # Enquanto 'ahead' não é None e 'ahead.next' não é None
            ahead = ahead.next.next # Avança 'ahead' duas vezes
            head = head.next # Avança 'head' uma vez
        return head # Retorna o nó no meio da lista
        