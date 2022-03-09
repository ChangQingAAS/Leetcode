class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.extend(s, i, i)
            res += self.extend(s, i, i + 1)
        return res

    def extend(self, s, i, j):
        res = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res