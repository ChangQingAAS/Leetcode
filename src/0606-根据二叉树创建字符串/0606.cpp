class Solution {
public:
    string tree2str(TreeNode* t) {

        if(t==nullptr)return "";
        if(t->left==nullptr&&t->right==nullptr){
            return to_string(t->val);
        }
        if(t->right==nullptr){
            return to_string(t->val)+("("+tree2str(t->left)+")");
        }
        return to_string(t->val)+("("+tree2str(t->left)+")"+"("+tree2str(t->right)+")");
    }
};

/*
四种情况:
    第一种情况是该节点为空或者左右子树都为空，这时既不需要加左括号也不需要加右括号，
    第二种情况是右子树为空时，这时左子树需要加括号，右子树不需要加括号
    
    当三种情况是左子树为空时，这时仍需要给左子树加括号表示左子树为空
    第四种情况当左右子树均不为空时，此时左右子树均需加括号
    第三四种情况可以合并在一起
*/