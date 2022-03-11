class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        ListNode *p = head;
        ListNode *s;
        if (p && p->next)
        {
            s = p->next;
            p->next = s->next;
            s->next = p;
            head = s;

            while (p->next && p->next->next)
            {
                s = p->next->next;
                p->next->next = s->next;
                s->next = p->next;
                p->next = s;
                p = s->next;
            }
        }
        return head;
    }
};