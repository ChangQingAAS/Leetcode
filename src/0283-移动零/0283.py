class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 新建一个数组
        res = [0 for x in range(len(nums))]
        index = 0
        for item in nums:
            if item != 0:
                res[index] = item
                index += 1
        nums[:] = res[:]
        # 双指针法
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1