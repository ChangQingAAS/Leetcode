class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #快慢指针
        #slow一次走一步
        #fast一次走两步 

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow