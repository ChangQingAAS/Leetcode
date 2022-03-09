class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        val_list = []
        while cur:
            var = cur.val
            val_list.append(var)
            cur = cur.next
        res = 0
        for index, item in enumerate(val_list[::-1]):
            res += item * (2**index)
        return res