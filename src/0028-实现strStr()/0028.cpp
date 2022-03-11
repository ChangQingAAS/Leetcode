class Solution
{
public:
    int strStr(string haystack, string needle)
    {
        int i = 0, j = 0;
        while (i < haystack.length() && j < needle.length())
        {
            if (needle[j] == haystack[i])
            {
                i++;
                j++;
            }
            else
            {
                i = i - j + 1;
                j = 0;
            }
        }
        if (j >= needle.length())
            return i - needle.length();
        else
            return -1;
    }
};