class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return 

        length = len(nums)
        middle = length // 2
        root = TreeNode(nums[middle])
        left = self.sortedArrayToBST(nums[:middle])
        right = self.sortedArrayToBST(nums[middle + 1:])
        if left:
            root.left = left
        if right:
            root.right = right
        return root
