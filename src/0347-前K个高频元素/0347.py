class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        time_dict = {}
        for num in nums:
            time_dict[num] = time_dict.get(num,0) + 1
        
        res_list = sorted(time_dict.items(), key = lambda x:x[1], reverse = True)
        
        ans  = []
        for i in range(0,k):
            ans.append(res_list[i][0])
        return ans