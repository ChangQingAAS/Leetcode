class Solution {
    vector<int> node;
public:
    int getMinimumDifference(TreeNode* root) {
        int ans = INT_MAX;
        Inorder(root);
        for(int i = 0; i< node.size();i++)
            for(int j = i + 1; j< node.size(); j++)
                ans = min(ans, abs(node[j] - node[i]));
        return ans;
    }
private:
    void Inorder(TreeNode* tree){
        if(tree == nullptr) return;
        node.push_back(tree->val);
        Inorder(tree->left);
        Inorder(tree->right);
    }
};