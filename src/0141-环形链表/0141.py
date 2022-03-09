# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        address_list = [id(head)]
        prev = head
        while prev:
            if not prev.next:
                return False
            id_ = id(prev.next)
            if id_ in address_list:
                return True
            else:
                address_list.append(id_)
            prev = prev.next