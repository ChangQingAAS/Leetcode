from queue import Queue 
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        node_queue = Queue()
        path_queue = Queue()
        node_queue.put(root)
        path_queue.put(str(root.val))

        ans = []
        while node_queue.qsize():
            node = node_queue.get()
            path = path_queue.get()
            if node.left is None and node.right is None:
                ans.append(path)
                continue
            if node.left:
                node_queue.put(node.left)
                path_queue.put(path + '->' + str(node.left.val))
            if node.right:
                node_queue.put(node.right)
                path_queue.put(path + '->' + str(node.right.val))
            
        return ans
