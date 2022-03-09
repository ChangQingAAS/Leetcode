class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        L = []
        length = len(nums)
        nums.sort()
        for i in range(0,length):
            # 遇见相同的数直接跳过
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length):
                # 遇见相同的数直接跳过
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                m = j +1
                n = length -1
                while m< n:
                    counter = nums[i] + nums[j] + nums[m] + nums[n]
                    # 跳重
                    if(m!= j + 1 and nums[m] == nums[m-1]) or counter < target:
                        m += 1 
…                   # 跳重
                    elif (n!= length -  1 and nums[n] == nums[n+1]) or counter > target:
                        n -= 1 
                    else :
                        L.append([nums[i],nums[j],nums[m],nums[n]])
                        m += 1
                        n -= 1  
        return L