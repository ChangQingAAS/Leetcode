class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_table = {}
        dissappear_nums = []
        for num in nums:
            hash_table[num] = '' 
        for item in range(1, len(nums) + 1):
            if item not in hash_table:
                dissappear_nums.append(item)
        return dissappear_nums