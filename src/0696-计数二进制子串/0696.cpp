class Solution
{
public:
    int countBinarySubstrings(string s)
    {
        int last = 0, cur = 1;
        int res = 0;
        for (int i = 1; i < s.size(); i++)
        {
            if (s[i] == s[i - 1])
                cur++;
            else
            {
                last = cur;
                cur = 1;
            }
            if (last >= cur)
                res++;
        }
        return res;
    }
};