class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        max_index = nums.index(max(nums))
        max_ = nums[max_index]
        nums.remove(max_)
        if len(nums) == 0:
            return -1
        _max_index = nums.index(max(nums))
        _max_ = nums[_max_index]
        if _max_ *2 > max_:
            return -1
        else:
            return max_index