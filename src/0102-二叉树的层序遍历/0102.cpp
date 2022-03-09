/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;

        if(root == nullptr)
            return ans;
        
        queue<TreeNode* > q;
        q.push(root);
        // 记录vector层数index
        int j = -1;

        //宽度优先搜索
        while(q.size() != 0)
        {
            j++;
            //记录本层有多少节点
            int size = q.size();
            // 初始化ans[j]
            ans.push_back(vector<int>(0));
            //依次遍历该层所有节点，pop掉该层所有节点，push下一层所有节点
            for(int i = 0; i< size; i++)
            {
                TreeNode* node = q.front();

                q.pop();

                ans[j].push_back(node->val);

                if(node->left != nullptr){
                    q.push(node->left);
                }

                if(node->right != nullptr){
                    q.push(node->right);
                }
            }
        }
        return ans;
    }
};