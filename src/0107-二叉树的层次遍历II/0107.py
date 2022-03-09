from queue import Queue


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = list()
        if not root:
            return ans

        q = Queue()
        q.put(root)

        while q.qsize():
            size = q.qsize()
            tmp = []
            for i in range(size):
                node = q.get()
                if node:
                    tmp.append(node.val)
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)
            if tmp:
                ans.append(tmp)

        ans.reverse()
        return ans