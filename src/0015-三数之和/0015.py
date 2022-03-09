class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        ans = []
        for i in range(length):
            # 如果排序后的第一个元素都大于0，则三数之和必然大于0
            if nums[i] > 0:
                continue
            # 跳过重复元素
            if i > 0 and nums[i] == nums[i -1]:
                continue

            L = i + 1
            R = length - 1
            while L < R:
                sum_ = nums[i] + nums[L] + nums[R]
                if sum_ < 0:
                    L += 1
                    continue
                elif sum_ > 0:
                    R -= 1
                    continue
                else:
                    ans.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                while L < R and nums[L] == nums[L-1]:
                        L += 1
                while L < R and nums[R] == nums[R+1]:
                    R -= 1
            
        return ans