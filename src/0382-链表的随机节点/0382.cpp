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
    ListNode* head;
public:
    Solution(ListNode* n):head(n) {
    }
    
    int getRandom() {
      int ans = head ->val;
      ListNode* node = head -> next;
      int i = 2;
      while(node){
        if((rand() % i) == 0){
          ans = node->val;
        }
        i++;
        node = node->next;
      }
      return ans;
    }
}; 
