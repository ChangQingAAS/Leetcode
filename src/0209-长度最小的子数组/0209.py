class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        ans = len(nums) + 1
        sum = 0

        for end in range(0, len(nums)):
            sum += nums[end]

            while sum >= target:
                # 窗口内的值总和满足条件
                win_length = end - start + 1
                ans = min(ans,win_length)
                sum -= nums[start]
                start += 1
            
        if ans > len(nums):
            return 0

        return ans

# * 定义窗口的起始指针和结束指针
# * 当窗口内的值总和小于目标值时，不断移动窗口的结束指针，扩大窗口
# * 当窗口内的值总和满足目标情况，不断移动起始指针，缩小窗口
# * 用一个变量记录最小窗口长度       