class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 方法一：利用哈希表统计元素个数，时间复杂度O(n)
        count_dict = {}
        for item in nums:
            count_dict[item] = count_dict.get(item,0) + 1
            if count_dict[item] > len(nums) /2:
                return item
        
        # 方法二：排序
        # 处于len(nums) /2位置的必是多数元素
        nums.sort()
        return nums[len(nums)//2]