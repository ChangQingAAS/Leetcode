class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        tmp_max_ones = 0
        for item in nums:
            if item == 1:
                tmp_max_ones += 1
            else:
                max_ones = max(max_ones, tmp_max_ones)
                tmp_max_ones = 0
            
        max_ones = max(max_ones, tmp_max_ones)
        return max_ones