from queue import Queue


# 递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 迭代
from queue import Queue


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = Queue()
        q.put(root)
        depth = 0

        while q.qsize():
            depth += 1
            size = q.qsize()
            for i in range(size):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

        return depth