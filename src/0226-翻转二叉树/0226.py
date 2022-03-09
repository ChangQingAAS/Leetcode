class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        q_ = [root]
        while q_:
            node = q_.pop()
            left = node.left
            right = node.right
            # 左右两个子节点交换
            node.left = right
            node.right = left
            if node.left:
                q_.append(node.left)
            if node.right:
                q_.append(node.right)
            
        return root