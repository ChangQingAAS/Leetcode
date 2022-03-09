class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # 剪枝情况：ransom长度大于magazine
        if len(ransomNote) > len(magazine):
            return False

        hash_1 = dict()
        hash_2 = dict()

        for char in ransomNote:
            hash_1[char] = hash_1.get(char,0) + 1
        for char in magazine:
            hash_2[char] = hash_2.get(char,0) + 1
        
        for char,times in hash_1.items():
            if times > hash_2.get(char,0):
                return False
        
        return True

# 算出每个字符的长度，然后比大小