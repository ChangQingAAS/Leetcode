from queue import Queue
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(p,q):
            if p is None and q is None:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                return isSame(p.left,q.left) and isSame(p.right, q.right)

        Q = Queue()
        Q.put(s)
        while Q.qsize():
            node = Q.get()
            if node.val == t.val:
                if isSame(node,t):
                    return True
                else:
                    if node.left:
                        Q.put(node.left)
                    if node.right:
                        Q.put(node.right)
            else:
                if node.left:
                    Q.put(node.left)
                if node.right:
                    Q.put(node.right)
        
        return False