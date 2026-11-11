# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        current = head

        while head:
            count += 1
            head.next
        
        div = count // 2

        while div != 0:
            div -= 1
            current.next
    
        return current
