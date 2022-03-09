class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        prevA = headA
        prevB = headB

        while prevA or prevB:
            if not prevA:
                prevA = headB 
            if not prevB:
                prevB = headA
            if prevB == prevA:
                return prevA
            
            prevA = prevA.next
            prevB = prevB.next
        return None
