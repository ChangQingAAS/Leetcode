class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val_list = []
        cur = head
        while cur:
            val_list.append(cur.val)
            cur = cur.next
        return val_list == val_list[::-1]