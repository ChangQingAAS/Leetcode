// 这道题可以看作是自己实现 C++ 里的 lower_bound 和 upper_bound 函数。这里我们尝试使用左闭右开的写法，当然左闭右闭也可以。
// 找上下区间。
class Solution
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        vector<int> res(2, -1);
        int n = nums.size();
        if (n == 0)
            return res;
        int lower = lower_bound(nums, target);
        if (lower == nums.size() || nums[lower] != target)
        {
            return res;
        }

        int upper = upper_bound(nums, target) - 1; //这里需要减一位
        return vector<int>{lower, upper};
    }

    int lower_bound(vector<int> &nums, int target)
    {
        int l = 0, r = nums.size(), mid;
        while (l < r)
        {
            mid = l + (r - l) / 2;
            if (nums[mid] >= target)
            {
                r = mid;
            }
            else
            {
                l = mid + 1;
            }
        }
        return l;
    }

    int upper_bound(vector<int> &nums, int target)
    {
        int l = 0, r = nums.size(), mid;
        while (l < r)
        {
            mid = l + (r - l) / 2;
            if (nums[mid] > target)
            {
                r = mid;
            }
            else
            {
                l = mid + 1;
            }
        }
        return l;
    }
};