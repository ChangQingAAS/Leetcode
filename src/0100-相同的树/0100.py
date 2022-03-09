from queue import Queue


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue_1 = Queue()
        queue_2 = Queue()
        if p:
            queue_1.put(p)
        if q:
            queue_2.put(q)

        while queue_1.qsize() and queue_2.qsize():
            node_1 = queue_1.get()
            node_2 = queue_2.get()

            if node_1.val != node_2.val:
                return False

            # 坑： None 做判断
            # 一个为None，另一个不为None
            if (not node_1.left) ^ (not node_2.left):
                return False
            if (not node_1.right) ^ (not node_2.right):
                return False

            if node_1.left:
                queue_1.put(node_1.left)
                queue_2.put(node_2.left)
            if node_1.right:
                queue_1.put(node_1.right)
                queue_2.put(node_2.right)
        if queue_1.qsize() or queue_2.qsize():
            return False

        return True