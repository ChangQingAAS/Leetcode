class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 对原数组进行排序，然后进行比较
        nums_ = nums.copy()
        nums.sort()
        start, end = 0,0
        flag = False # 区分start还是end阶段
        for index, item in enumerate(nums_):
            if item != nums[index]:
                if not flag:
                    start = index
                    flag = True
                else:
                    end = index + 1
        return end - start