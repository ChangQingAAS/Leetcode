class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        for i,item in enumerate(numbers):
            last = target - item
            if last in num_dict:
                return [num_dict[last]+1,i+1]
            else:
                num_dict[item] = i

        return []