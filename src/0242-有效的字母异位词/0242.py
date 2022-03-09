class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if s == t:
            return True

        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1

        return hash_t == hash_s