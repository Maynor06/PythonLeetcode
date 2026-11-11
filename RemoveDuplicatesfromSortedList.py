# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:

        if head is None:
            return head

        dummy = head
        current = dummy

        while current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy

