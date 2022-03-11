class Solution
{
public:
    vector<int> preorderTraversal(TreeNode *root)
    {
        vector<int> ret;
        if (!root)
            return ret;
        deque<TreeNode *> s;
        s.push_front(root);
        while (!s.empty())
        {
            TreeNode *node = s.front();
            s.pop_front();
            ret.push_back(node->val);
            cout << " " << node->val;
            if (node->right)
            {
                s.push_front(node->right);
            }
            if (node->left)
            {
                s.push_front(node->left);
            }
        }
        return ret;
    }
};