from queue import Queue


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def isLeavesNode(node):
            if node.left is None and node.right is None:
                return True
            return False

        if not root:
            return 0

        res = 0
        q = Queue()
        q.put(root)

        while q.qsize():
            node = q.get()
            if node.left:
                if isLeavesNode(node.left):
                    res += node.left.val
                else:
                    q.put(node.left)

            if node.right:
                if not isLeavesNode(node.right):
                    q.put(node.right)
        return res