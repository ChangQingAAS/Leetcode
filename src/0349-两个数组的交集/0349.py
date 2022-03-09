class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        # 遍历短的集合更快
        if len(set1) < len(set2):
            return [item for item in set1 if item in set2]
        return [item for item in set2 if item in set1]
            