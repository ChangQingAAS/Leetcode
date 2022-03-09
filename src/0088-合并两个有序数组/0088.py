class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 双指针法，从后往前遍历，哪个元素大就把这个元素放在最后：

        p1 = m -1
        p2 = n -1
        p = m + n -1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -=1

        # 退出循环有两种情况 p1 <0 or p2<0
        # p1 <0 说明nums1大已经放在后面，需要在前面放p2
        if p1 < 0:
            nums1[:p2+1] = nums2[:p2+1]
        if p2 < 0:
            pass
        return nums1