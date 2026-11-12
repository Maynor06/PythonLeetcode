# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA = headA
        pB = headB


        while pA != pB:
            # Si pA llega al final, lo saltamos al inicio de B. Si no, avanza un paso.
            pA = pA.next if pA else headB
            
            # Si pB llega al final, lo saltamos al inicio de A. Si no, avanza un paso.
            pB = pB.next if pB else headA

        return pA # Puede ser el nodo de intersección o None
