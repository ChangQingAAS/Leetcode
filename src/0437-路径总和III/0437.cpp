class Solution
{
public:
    int pathSum(TreeNode *root, int sum)
    {
        return root ? pathSum_(root, sum) + pathSum(root->left, sum) + pathSum(root->right, sum) : 0;
    }

    int pathSum_(TreeNode *root, int sum)
    {
        if (!root)
        {
            return 0;
        }
        int count = root->val == sum ? 1 : 0;
        count += pathSum_(root->left, sum - root->val);
        count += pathSum_(root->right, sum - root->val);
        return count;
    }
};