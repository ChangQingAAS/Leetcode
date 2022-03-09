from queue import Queue
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = Queue()
        q.put(root)
        ans = 0
        while q.qsize():
            size = q.qsize()
            for _ in range(size):
                node = q.get()
                ans += 1
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
    
        return ans