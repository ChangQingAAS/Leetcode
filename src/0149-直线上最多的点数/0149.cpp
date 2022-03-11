class Solution
{
public:
    int maxPoints(vector<vector<int>> &points)
    {
        unordered_map<double, int> hash; // <斜率,点个数>
        int max_count = 0, same = 1, same_y = 1;
        for (int i = 0; i < points.size(); i++)
        {
            same = 1, same_y = 1;
            for (int j = i + 1; j < points.size(); j++)
            {
                if (points[i][1] == points[j][1])
                {
                    same_y++;
                    if (points[i][0] == points[j][0])
                    {
                        same++;
                    }
                }
                else
                {
                    double dx = points[i][0] - points[j][0];
                    double dy = points[i][1] - points[j][1];
                    ++hash[dx / dy];
                }
            }
            max_count = max(max_count, same_y);
            for (auto item : hash)
            {
                max_count = max(max_count, same + item.second);
            }
            hash.clear();
        }
        return max_count;
    }
};