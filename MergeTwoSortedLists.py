# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        lresult: ListNode | None = None

        while list1 or list2:
            if list1.val < list2.val:
                if not lresult:
                    lresult = ListNode(list1.val)
                    current = lresult
                else:
                    current.next = ListNode(list1.val)
                    current = current.next
                list1 = list1.next
            if list2.val < list1.val:
                if not lresult:
                    lresult = ListNode(list2.val)
                    current = lresult
                else:
                    current.next = ListNode(list2.val)
                    current = current.next

                list2 = list2.next
            else:
                if not lresult:
                    lresult = ListNode(list2.val)
                    current = lresult
                else:
                    current.next = ListNode(list2.val)
                    current = current.next
                list1 = list1.next
        return lresult

def main(): 
    A = ListNode(1, ListNode(2, ListNode(4)))
    V = ListNode(1, ListNode(3, ListNode(4)))

    S = Solution()
    result = S.mergeTwoLists(A, V)
    print(result)


main()
