class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    # 如果当前元素的前一个元素大于0，就将当前元素加上前一个元素。

    """
    从左加到右：
    [-2,1,-3,4,-1,2,1,-5,4]
    [-2,1,-2,4, 3,5,6, 1,5]
    """
     for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)

    """
    从右加到左：
    [-2,1,-3,4,-1,2,1,-5,4]
    [2,4,3,6,2,3,1,-1,4]
    """

        for i in range(len(nums)-2,-1,-1):
            if nums[i + 1] > 0 :
                nums[i] += nums[i + 1]
        
        return max(nums)