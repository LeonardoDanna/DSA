# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head: # if the linked list is empty
            return None

        current = head # current node is the head

        while current and current.next: 
            if current.val == current.next.val: # if the current node's value is equal to the next node's value
                current.next = current.next.next # skip the next node
            else:
                current = current.next # move to the next node

        return head