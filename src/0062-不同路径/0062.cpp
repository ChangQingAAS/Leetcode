class Solution
{
public:
    int uniquePaths(int m, int n)
    {
        vector<vector<int>> map(m + 1, vector<int>(n + 1));

        map[1][1] = 1;
        for (int i = 1; i <= m; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                if (i == 1 && j == 1)
                    continue;
                else
                    map[i][j] = map[i - 1][j] + map[i][j - 1];
            }
        }
        return map[m][n];
    }
};