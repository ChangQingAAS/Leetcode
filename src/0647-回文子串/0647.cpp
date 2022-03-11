class Solution
{
public:
    int countSubstrings(string s)
    {
        int count = 0;
        for (int i = 0; i < s.length(); i++)
        {
            count += extendSubString(s, i, i);     // 奇数长度
            count += extendSubString(s, i, i + 1); // 偶数长度
        }
        return count;
    }

    int extendSubString(string s, int l, int r)
    {
        int count = 0;
        while (l >= 0 && r < s.length() && s[l] == s[r])
        {
            l--;
            r++;
            count++;
        }
        return count;
    }
};