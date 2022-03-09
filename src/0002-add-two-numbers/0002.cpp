/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode *dummyHead = new ListNode(-1);
        ListNode* result = dummyHead;
        int carried = 0;
        while(l1 || l2)
        {
            // set cur value
            int val_l1 = l1 ? l1->val : 0;
            int val_l2 = l2 ? l2->val : 0;
            result->next = new ListNode((val_l1 + val_l2 + carried) %10);
            carried = (val_l1 + val_l2 + carried) / 10;

            //update
            result = result->next;
            l1 = l1 ? l1->next : NULL;
            l2 = l2 ? l2->next : NULL;
        }
        // set lastest value
        result->next = carried ? new ListNode(carried) : NULL;
        // 返回头结点
        ListNode * ret = dummyHead->next;
        return ret;
    }
};

// 直接建个新链表就行，这里的坑是返回的是头结点.需要建一个等待被删的节点，后面是result，然后再通过它拿到result