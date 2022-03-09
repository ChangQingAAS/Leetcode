class Solution
{
    /**
       贪心法, 每个气球只少需要一支箭, 先按照右端点排序, 然后每次
       从最小的右端点射出一支箭, 去掉被射爆的气球, 重复该过程.
       **/
private:
    static bool cmp(const vector<int> &a, const vector<int> &b)
    {
        return a[1] < b[1];
    }

public:
    int findMinArrowShots(vector<vector<int>> &points)
    {
        if (points.size() == 0)
            return 0;

        sort(points.begin(), points.end(), cmp);

        int result = 1; // points 不为空至少需要一支箭
        int axis = points[0][1];

        for (int i = 1; i < points.size(); i++)
        {
            if (axis < points[i][0])
            {
                result++; // 需要一支箭
                axis = points[i][1];
            }
        }
        return result;
    }
};