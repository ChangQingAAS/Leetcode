class Solution
{
public:
    int mySqrt(int a)
    {
        if (a == 0)
            return 0;
        int l = 1, r = a;
        int mid;
        while (l <= r)
        {
            // mid = (l + r) / 2; //有溢出
            mid = l + (r - l) / 2;
            if (a / mid == mid)
            {
                return mid;
            }
            else if (mid > a / mid)
            {
                r = mid - 1;
            }
            else
            {
                l = mid + 1;
            }
        }
        return r;
    }
};

// f(x) = x^2 − a = 0 的解。因为我们只考 虑 x ≥ 0，所以 f(x) 在定义域上是单调递增的。
// 考虑到 f(0) = −a ≤ 0， f(a) = a^2 − a ≥ 0，我们 可以对[0, a] 区间使用二分法找到 f(x) = 0 的解。