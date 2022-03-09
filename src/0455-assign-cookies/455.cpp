// 给饥饿度最小的孩子能满足他的最小饼干，所以要对数组进行排序

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // 首先需要给这两个数组排序
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int g_index = 0;
        int s_index = 0;
        while(g_index < g.size() && s_index < s.size()){
            // 如果满足则指针后移
            // 由于排好序了，所以指针位置就是能吃饱的孩子数
            // 如果当前孩子吃不饱，后面的孩子必然也吃不饱
            if (g[g_index] <= s[s_index])
                g_index++;
            // 饼干指针后移
            s_index++;
        }
        return g_index;
    }
};