class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        int l = 0, r = nums.size() - 1;
        int target = nums.size() - k;
        while (l < r)
        {
            int mid = QuickSelection(nums, l, r);
            if (mid == target)
            {
                return nums[mid];
            }
            else if (mid < target)
            {
                l = mid + 1;
            }
            else
            {
                r = mid - 1;
            }
        }
        return nums[l];
    }

    int QuickSelection(vector<int> &nums, int l, int r)
    {
        int i = l + 1, j = r;
        while (true)
        {
            while (i < r && nums[i] <= nums[l])
            {
                i++;
            }
            while (j > l && nums[j] >= nums[l])
            {
                j--;
            }
            if (i >= j)
            {
                break;
            }
            swap(nums[i], nums[j]);
        }
        swap(nums[l], nums[j]);
        return j;
    }
};

// 快速选择一般用于求解 k-th Element 问题，可以在 O(n) 时间复杂度，O(1) 空间复杂度完成求
// 解工作。快速选择的实现和快速排序相似，不过只需要找到第 k 大的枢（pivot）即可，不需要对
// 其左右再进行排序。与快速排序一样，快速选择一般需要先打乱数组，否则最坏情况下时间复杂
// 度为 O(n^2)，我们这里为了方便省略掉了打乱的步骤。
