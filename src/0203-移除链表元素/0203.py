class Solution():
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        start = ListNode(0) # 虚拟头结点
        cur_node = start
        cur_node.next = head
        while cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return start.next