class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    # 把四数之和转变成两数之和，即AB一组，CD一组
    # 先把AB合在一起，再遍历CD，显然复杂度:O(n^4) -> O(n^2)了
        hash_1 = dict()
        for index_a, item_a in enumerate(A):
            for index_b,item_b in enumerate(B):
                sum = item_a + item_b
                hash_1[sum] = hash_1.get(sum,0) + 1
            
        ans = 0
        for index_c, item_c in enumerate(C):
            for index_d,item_d in enumerate(D):
                sum = item_c + item_d
                if (0 - sum) in hash_1:
                    ans += hash_1[0 -sum]
                
        return ans