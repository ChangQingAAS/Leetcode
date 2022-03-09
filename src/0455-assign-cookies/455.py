class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_index, s_index = 0, 0
        while g_index < len(g) and s_index < len(s):
            if g[g_index] <= s[s_index]:
                g_index += 1
            s_index += 1

        return g_index


# 贪心：给剩余孩子里最小饥饿度的孩子分配最小的能饱腹的饼干