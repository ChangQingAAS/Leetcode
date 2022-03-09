from queue import Queue


class Solution:
    def minDepth(self, root: TreeNode) -> int:
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
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

        return depth