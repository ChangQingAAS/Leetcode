class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {},{},{}
        # 遍历数组，记录元素第一次出现和最后一次出现的位置，以及元素出现的次数
        for i,item in enumerate(nums):
            if item not in left:
                left[item] = i
            right[item] = i
            count[item] = count.get(item,0) +1

        min_len = len(nums)
        # 找出出现次数最多的元素
        max_items = max(count.values())
        for item, times in count.items():
            if times == max_items:
                min_len = min(right[item] - left[item] + 1, min_len)
        
        return min_len
