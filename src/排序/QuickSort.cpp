#include <iostream>
#include <vector>
using namespace std;

// 左闭右闭的二分写法
void quick_sort(vector<int> &nums, int l, int r)
{
    if (l + 1 >= r)
    {
        return;
    }
    int first = l, last = r - 1;
    int key = nums[first];
    while (first < last)
    {
        while (first < last && nums[last] >= key)
        {
            --last;
        }
        nums[first] = nums[last];
        while (first < last && nums[first] <= key)
        {
            ++first;
        }
        nums[last] = nums[first];
    }
    // 此时first == last，即为放key的地方
    nums[first] = key;
    quick_sort(nums, l, first);
    quick_sort(nums, first + 1, r);
}

void print_array(vector<int> &nums)
{
    for (int i = 0; i < nums.size(); i++)
    {
        cout << nums[i] << " ";
    }
    cout << endl;
}

int main(int argc, char **argv)
{
    vector<int> nums{2, 4, 6, 8, 5, 3, 7};
    int l = 0, r = nums.size() - 1;
    quick_sort(nums, l, r);
    print_array(nums);
}