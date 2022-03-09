#include <iostream>
#include <vector>
using namespace std;

// 左闭右闭？
void merge_sort(vector<int> &nums, int l, int r, vector<int> &temp)
{
    if (l + 1 >= r)
    {
        return;
    }
    // divide
    int m = l + (r - l) / 2;
    merge_sort(nums, l, m, temp);
    merge_sort(nums, m, r, temp);
    // conquer
    int p = l, q = m;
    int i = l;
    // 两个counter都超出界限，则退出循环
    while (p < m || q < r)
    {
        //  为方便理解，没有合并if
        if (p < m && nums[p] <= nums[q])
        {
            temp[i++] = nums[p++];
        }
        else if (q < r && nums[p] > nums[q])
        {
            temp[i++] = nums[q++];
        }
        else if (q >= r)
        {
            temp[i++] = nums[p++];
        }
        else
        {
            temp[i++] = nums[q++];
        }
    }

    for (int j = l; j < r; j++)
    {
        nums[j] = temp[j];
    }
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
    vector<int> temp(nums.size(), -1);
    int l = 0, r = nums.size();
    merge_sort(nums, l, r, temp);
    print_array(nums);
}