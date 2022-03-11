class Solution
{
public:
    // 转化问题：：记录两个字符串每个位置的字符第一次出现的位置，如果两个字符串中相同位置的字符与它们第一次出现的位置一样
    bool isIsomorphic(string s, string t)
    {
        vector<int> s_first(256, INT_MAX), t_first(256, INT_MAX);
        for (int i = 0; i < s.length(); i++)
        {
            if (s_first[s[i]] != t_first[t[i]])
            {
                return false;
            }
            s_first[s[i]] = t_first[t[i]] = i + 1;
        }
        return true;
    }
};