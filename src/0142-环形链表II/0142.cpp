// Floyd判圈法
class Solution
{
public:
    ListNode *detectCycle(ListNode *head)
    {
        ListNode *slow = head;
        ListNode *fast = head;
        // 判断是否存在环路
        do
        {
            // fast无法增长，说明链表结束
            if (!fast || !fast->next)
                return NULL;
            fast = fast->next->next;
            slow = slow->next;
        } while (fast != slow);
        // 如果存在环路，寻找环路节点
        fast = head;
        while (fast != slow)
        {
            fast = fast->next;
            slow = slow->next;
        }
        return fast;
    }
};