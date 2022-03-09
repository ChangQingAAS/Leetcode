class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## 三步反转：
        # 第一步，反转整个数组
        # 第二步，反转nums[:k]
        # 第三步，反转nums[k:]

        length = len(nums)
        k = k % length
        if k == 0:
            return nums
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums