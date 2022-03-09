class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for index, item in enumerate(nums):
            if item % 2 == 0:
                nums[i], nums[index] = item, nums[i]
                i += 1
        return nums

# 原地修改数组，遍历数组，当遇到第一个偶数时，就把这个偶数放在数组第一个位置，当遇到第二个偶数，就把这个偶数放在数组第二个位置。