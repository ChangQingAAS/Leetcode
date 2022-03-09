class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
    # 1. 遍历数组，两个集合，一个集合(diff)保存diff对中最小的元素，一个集合(saw)保存已经遍历过的元素。用集合是为了避免重复
    # 2. 如果x-k in saw,保存x-k到diff中。
    # 3. 如果x+k in saw,保存x到diff中。
    # 4. 返回diff的长度.
        if k < 0:
            return 0
        diff = set()
        saw = set()
        c = 0
        for item in nums:
            if(item - k) in saw:
                diff.add(item - k)
            if(item + k)  in saw:
                diff.add(item)
            saw.add(item)
        return len(diff)
