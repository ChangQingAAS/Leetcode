class Solution():
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(0)
        prev = prehead

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2

        return prehead.next