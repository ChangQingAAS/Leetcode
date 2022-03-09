# 利用两个指针的距离差找到倒数第n个节点的前一个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_0 = ListNode(0)
        node_0.next = head
        first = node_0
        second = node_0
        for _ in range(n):
            first = first.next

        while first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next
    
        return node_0.next