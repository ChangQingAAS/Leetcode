class Solution
{
public:
    int lengthOfLIS(vector<int> &nums)
    {
        // dp表示表示以 i 结尾，最长子序列长度
        int max_len = 0;
        int n = nums.size();
        if (n <= 1)
            return n;
        vector<int> dp(n, 1);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (nums[i] > nums[j])
                {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }

            max_len = max(max_len, dp[i]);
        }
        return max_len;
    }
};