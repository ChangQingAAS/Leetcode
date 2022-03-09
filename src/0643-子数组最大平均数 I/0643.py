class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[:k])
        max_ = sum_
        for i in range(k, len(nums)):
            sum_ = sum_ + nums[i] - nums[i-k]
            max_ = max(sum_, max_)
        return max_ / k

        