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
class Solution
{
public:
    int depth(TreeNode *tree, int &ans)
    {
        if (tree == nullptr)
            return 0;

        int left = depth(tree->left, ans);
        int right = depth(tree->right, ans);
        ans = max(ans, left + right);
        return max(left, right) + 1;
    }

    int diameterOfBinaryTree(TreeNode *root)
    {
        int ans = 0;
        depth(root, ans);
        return ans;
    }
};