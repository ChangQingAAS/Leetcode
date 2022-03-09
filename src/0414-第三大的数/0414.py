class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 法1：去重，排序
        nums = list(set(nums))
        nums.sort()
        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]

        #法2：定义3个变量存储最大的三个数：
        m1 = float("-inf")
        m2 = float("-inf")
        m3 = float("-inf")
        for item in nums:
            if item > m1:
                m3 = m2
                m2 = m1
                m1 = item
            elif m2 < item <m1:
                m3 = m2
                m2 = item
            elif m3 < item <m2:
                m3 = item
            
        # 只有两个的情况
        if m3 == float("-inf"):
            return m1
        
        return m3
