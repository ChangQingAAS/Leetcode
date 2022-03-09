class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        target_sum = (l + 1) * l / 2
        curr_sum = sum(nums)
        return int(target_sum - curr_sum)