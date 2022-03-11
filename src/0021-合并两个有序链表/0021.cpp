class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode *dummy = new ListNode(0);
        ListNode *node = dummy;
        while (l1 && l2)
        {
            if (l1->val <= l2->val)
            {
                node->next = l1;
                l1 = l1->next;
                node = node->next;
            }
            else
            {
                node->next = l2;
                l2 = l2->next;
                node = node->next;
            }
        }
        node->next = l1 ? l1 : l2;
        return dummy->next;
    }
};