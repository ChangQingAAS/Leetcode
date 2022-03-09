class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, m = 0, 0
        for i in range(len(s)):
            left, right = i, i
            # 找到xyyx形式中的yy的坐标
            while left >= 0 and s[left] == s[i]:
                left -= 1
            while right < len(s) and s[right] == s[i]:
                right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if m - n + 1 < (right - 1) - (left + 1) + 1:
                # 得把多余的操作找回来
                n, m = left + 1, right - 1
        return s[n:m + 1]
