class Solution
{
public:
    int eraseOverlapIntervals(vector<vector<int>> &intervals)
    {
        if (intervals.empty()){
            return 0;
        }

        int n = intervals.size();
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b)
             { return a[1] < b[1]; });

        int result = 0;
        int prev = 0;
        // 因为定义好了位置，所以这里从第二个区间开始
        for (int i = 1; i < n; i++)
        {
            // 如果这样，就需要把intervals[i]删掉才行，即result++
            if (intervals[i][0] < intervals[prev][1])
            {
                result++;
            }
            //满足要求，则后移
            else
            {
                prev = i;
            }
        }
        return result;
    }
};

// 题解
// 在选择要保留区间时，区间的结尾十分重要：选择的区间结尾越小，余留给其它区间的空间就越大，就越能保留更多的区间。
// 因此，我们采取的贪心策略为，优先保留结尾小且不相交的区间。

// 具体实现方法为，先把区间按照结尾的大小进行增序排序，每次选择结尾最小且和前一个选择的区间不重叠的区间。
// 我们这里使用 C++ 的 Lambda，结合 std::sort() 函数进行自定义排序。

// 在样例中，排序后的数组为 [[1,2], [1,3], [2,4]]。按照我们的贪心策略，首先初始化为区间
// [1,2]；由于 [1,3] 与 [1,2] 相交，我们跳过该区间；由于 [2,4] 与 [1,2] 不相交，我们将其保留。因
// 此最终保留的区间为 [[1,2], [2,4]]。

// 这个贪心解法比较直接，不过好在顺利AC
// 更好的解法是：1.动态规划 2.贪心中，按开始进行排序或按可以通过的进行计数，然后（res = len - accepted)
