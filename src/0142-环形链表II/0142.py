class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_dict = {}
        while head:
            if head in node_dict:
                return head
            node_dict[head] = ''
            head = head.next

        return None