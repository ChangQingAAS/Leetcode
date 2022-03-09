class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        if length <= 1:
            return length

        nums = [1] * length
        for i in reversed(range(1, length)):
            if ratings[i - 1] > ratings[i]:
                nums[i - 1] = nums[i] + 1

        for i in range(0, length - 1):
            if ratings[i + 1] > ratings[i]:
                nums[i + 1] = max(nums[i + 1], nums[i] + 1)

        return sum(nums)


# 两次遍历即可：把所有孩子的糖果数初始化为 1；
# 先从左往右遍历一遍，如果右边孩子的评分比左边的高，则右边孩子的糖果数更新为左边孩子的糖果数加 1；
# 再从右往左遍历一遍，如果左边孩子的评分比右边的高，且左边孩子当前的糖果数不大于右边孩子的糖果数，则左边孩子的糖果数更新为右边孩子的糖果数加 1。
# 通过这两次遍历，分配的糖果就可以满足题目要求了。
# 这里的贪心策略即为，在每次遍历中，只考虑并更新相邻一侧的大小关系。