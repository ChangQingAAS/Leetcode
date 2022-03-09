class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = list()
        if not root:
            return ans

        stack = []
        node = root
        while stack or node:
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
            
        return ans