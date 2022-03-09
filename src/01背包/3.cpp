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
                dp[i][j] = max(dp[i - 1][j], dp[i][j - w] + v);
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    return dp[N][N];
}
// 完全背包，一个物品可以拿多次，只修改了动态方程

// 0-1 背包对物品的迭代放在外层，里层的体积或价值逆向遍历；
// 完全背包对物品的迭代放在里层，外层的体积或价值正向遍历。