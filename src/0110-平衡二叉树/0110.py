class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        if not root:
            return True
        left = root.left
        right = root.right

        return self.isBalanced(left) and self.isBalanced(right)  and abs(depth(left) - depth(right)) <= 1