int knapsack(vector<int> weights, vector<int> values, int N, int W)
{
    vector<int> dp(W + 1, 0);
    for (int i = 1; i <= N; i++)
    {
        int w = weights[i - 1];
        int v = values[i - 1];
        for (int j = W; j >= w; j--)
        {
            dp[j] = max(dp[j], dp[j - w] + v);
        }
    }
    return dp[w];
}