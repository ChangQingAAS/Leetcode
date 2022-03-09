class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in nums_hash:
                return [nums_hash[dif],i]
            nums_hash[nums[i]] = i
        return []

# 用字典存储每个元素及其对应的索引。时间复杂度O(n),空间复杂度O(n)

# * 从前向后依次遍历数组中的元素。
# * 计算差值，如果差值不存在字典中，则保存当前遍历的元素到字典中。
# * 如果差值存在字典中，返回差值的索引与当前元素的索引。