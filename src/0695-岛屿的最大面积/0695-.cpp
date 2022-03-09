class Solution
{
public:
    vector<int> direction{-1, 0, 1, 0, -1};

    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int m = grid.size(), n = m ? grid[0].size() : 0;
        int local_area = 0, area = 0;
        int x, y;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j])
                {
                    stack<pair<int, int>> island;
                    local_area = 1;
                    grid[i][j] = 0;
                    island.push({i, j});
                    while (!island.empty())
                    {
                        auto [r, c] = island.top();
                        island.pop();
                        for (int k = 0; k < 4; k++)
                        {
                            x = r + direction[k];
                            y = c + direction[k + 1];
                            if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1)
                            {
                                local_area++;
                                grid[x][y] = 0;
                                island.push({x, y});
                            }
                        }
                    }
                    area = max(local_area, area);
                }
            }
        }
        return area;
    }
};