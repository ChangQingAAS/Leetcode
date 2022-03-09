# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(node_1, node_2):
            # 都为None
            if node_1 is None and node_2 is None:
                return True
            # 一个是一个不是
            elif not node_1 or not node_2:
                return False
            if node_1.val != node_2.val:
                return False
            return check(node_1.left, node_2.right) and check(
                node_1.right, node_2.left)

        res = check(root.left, root.right)
        return res


# 迭代
from queue import Queue


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        1.两个队列分别存储根节点的左子节点和右子节点
        2.分别从两个队列中取出一个节点，进行比较
            2.1如果两个节点一个为None，一个不为None，则说明不对称，直接返回False
            2.2如果两个节点都不为None，比较节点值，如果值不相等，则说明不对称，直接返回False
            2.3如果值相等，按照顺序，添加节点的子节点到队列中，等待下一轮比较
        """

        left = root.left
        right = root.right
        queue_1 = Queue()
        queue_2 = Queue()
        queue_1.put(left)
        queue_2.put(right)

        while queue_1.qsize() and queue_2.qsize():
            node_1 = queue_1.get()
            node_2 = queue_2.get()
            if node_1 is None and node_2 is None:
                continue
            elif not node_1 or not node_2:
                return False
            elif node_1.val != node_2.val:
                return False

            queue_1.put(node_1.left)
            queue_2.put(node_2.right)

            queue_1.put(node_1.right)
            queue_2.put(node_2.left)

        return True
