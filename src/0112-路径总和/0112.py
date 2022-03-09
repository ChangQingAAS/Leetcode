from queue import Queue
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        node_queue = Queue()
        sum_queue = Queue()
        node_queue.put(root)
        sum_queue.put(root.val)

        while node_queue.qsize():
            node = node_queue.get()
            sum_ = sum_queue.get()
            if node.left is None and node.right is None:
                if sum_ == targetSum:
                    return True 
                
            if node.left:
                node_queue.put(node.left)
                sum_queue.put(sum_ + node.left.val)
            if node.right:
                node_queue.put(node.right)
                sum_queue.put(sum_ + node.right.val)

        return False
