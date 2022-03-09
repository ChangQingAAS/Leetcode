class Solution {
    int sum = 0;
public:
    void dfs(TreeNode* tree, int num){
        if(tree == nullptr) return;

        num = (num << 1) + tree->val;

        // 如果是叶子节点，则+= sum
        if(tree->left == nullptr && tree-> right == nullptr){
            sum += num;
            return;
        }

        dfs(tree->left, num);
        dfs(tree->right, num);

        return;
    }

    int sumRootToLeaf(TreeNode* root) {
        dfs(root, 0);
        return sum;
    }
};

return ((flipEquiv(root1->left,root2->right)&&flipEquiv(root1->right,root2->left))
                ||(flipEquiv(root1->left,root2->left)&&flipEquiv(root1->right,root2->right)));