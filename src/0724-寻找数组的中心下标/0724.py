class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        sum_ = sum(nums)
        
        # 第一个元素为中心索引的情况
        if sum_ == nums[0]:
            return 0

        # 其他情况
        left_sum = 0
        for i in range(len(nums) -1):
            left_sum += nums[i]
            if sum_ - nums[i+1] == left_sum * 2:
                return i+1

        
        # 最后一个元素为中心索引的情况
        if sum_ == nums[-1]:
            return len(nums) -1

        return -1

#### 分析：

# * 特殊情况是数组两边的元素为中心索引
# * 当第一个元素是中心索引，则其余元素之和为0，数组的总和=第一个元素。
# * 当最后一个元素是中心索引，同理。
# * 当中间的元素是中心索引时，数组的和-中心索引元素 = 左边元素和 * 2