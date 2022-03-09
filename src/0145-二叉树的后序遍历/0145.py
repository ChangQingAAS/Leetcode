class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = list()
        if not root:
            return ans

        stack = []
        node = root
        prev = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == prev:
                ans.append(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right

        return ans