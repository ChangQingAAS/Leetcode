# 层序遍历，队列中存放的都是同一层的节点，每一层第一个节点就是最左边的节点
from queue import Queue


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = None

        q = Queue()
        q.put(root)
        while q.qsize():
            size = q.qsize()
            for i in range(size):
                node = q.get()
                if i == 0:
                    ans = node.val
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

        return ans
