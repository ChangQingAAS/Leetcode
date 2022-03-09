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
    TreeNode* invertTree(TreeNode* root) {
        invert(root);
        return root;
    }
private:
    void invert(TreeNode*& tree)
    {
        if(tree == nullptr)
            return;
        TreeNode* leftTree = tree->left;
        tree->left = tree->right;
        tree->right = leftTree;

        invert(tree->left);
        invert(tree->right);
    }
};