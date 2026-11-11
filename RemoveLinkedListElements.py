class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # Remove the node
            else:
                current = current.next  # Move to the next node

        return dummy.next