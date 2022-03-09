#include <iostream>
#include <vector>
using namespace std;

void selection_sort(vector<int> &nums, int n)
{
    int minIndex;
    for (int i = 0; i < n - 1; i++)
    {
        minIndex = i;
        // 找到后续数组的最小元素下标
        for (int j = i + 1; j < n; j++)
        {
            if (nums[j] < nums[minIndex])
            {
                minIndex = j;
            }
        }
        // 把当前最小元素放到已排序的数组的后面
        swap(nums[minIndex], nums[i]);
    }
}

void print_array(vector<int> &nums)
{
    for (int i = 0; i < nums.size(); i++)
        cout << nums[i] << " ";
    cout << endl;
}

int main(int argc, char **argv)
{
    vector<int> nums{2, 4, 6, 8, 5, 3, 7};
    selection_sort(nums, nums.size());
    print_array(nums);
}