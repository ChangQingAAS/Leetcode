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
    bool isSymmetric(TreeNode* root) {
        return check(root, root);
    }
private:
    bool check(TreeNode* tree, TreeNode* root){
        if(!tree && !root)
            return true;
        if(tree == nullptr || root == nullptr)
            return false;
        return (tree->val == root->val) && check(tree->left, root->right) && check(tree->right, root->left);
    }
};