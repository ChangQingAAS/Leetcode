class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverseS(ss):
            ss = list(ss)
            L = 0
            R = len(ss) -1
            while L < R:
                ss[L],ss[R] = ss[R],ss[L]
                L += 1
                R -= 1
            return ''.join(ss)

        # 按照2k的长度进行遍历
        for i in range(0,len(s),2*k):
            s1 = s[i:i+2*k]
            if len(s1) < k:
                s1 = reverseS(s1)
            else:
                s1 = reverseS(s1[:k]) + s1[k:]
            s = s[:i] + s1 + s[i+2*k:]
        return s
        
