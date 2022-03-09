class Solution:
    def searchInsert(nums, target):
        # 1.目标值在数组所有元素之前
        # 2.目标值等于数组中元素
        # 3.目标值介于数组元素之间
        # 4.目标值在数组所有元素之后
        for i, item in enumerate(nums):
            # 前三中情况
            if item >= target:
                return i

        # 第四种情况
        return len(nums)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        二分查找:
        设定坐下标left和右下标right，计算中间下标mid。
        nums[mid]等于目标值，直接返回mid。
        nums[mid]大于目标值，则right左移。
        nums[mid]小于目标值，则left右移。
        查找结束没有值相等，返回left
        记住下列模板:
        """
        left = 0
        # 记得减1 
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        # target 不在当前nums.min ~ nums.max，则必然在0 or len(nums)，
        # 如果是0，则left不动，如果是len(nums)则right不动，left移到最后面
        return left