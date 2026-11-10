class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        lresult: ListNode | None = None
        count = 0
        while l1 or l2 or count:
            if l1:
                count += l1.val
                l1 = l1.next
            if l2:
                count += l2.val
                l2 = l2.next
            if not lresult:
                lresult = ListNode(count % 10)
                current = lresult
            else:
                current.next = ListNode(count % 10)
                current = current.next
            count //= 10

        return lresult