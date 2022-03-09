class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #利用哈希表
        hash_ = {}
        for index,item in enumerate(nums):
            # 如果不在就加入
            if item not in hash_:
                hash_[item] = index
            else:
                if index - hash_[item] <= k:
                    return True
                else:
                    # 因为是按index递增的方式前进的，所以不过不匹配证明原来的hash_[item]必然没有用了，肯定>k了，可以更换索引
                    hash_[item] = index
        
        return False