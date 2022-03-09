int knapsack(vector<int> weights, vector<int> values, int N, int W)
{
    vector<vector<int>> dp(N + 1, vector<int>(W + 1, 0));
    for (int i = 1; i <= N; i++)
    {
        int w = weights[i - 1], v = values[i - 1];
        for (int j = 1; j <= W; j++)
        {
            if (j >= w)
            {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v);
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    return dp[N][N];
}