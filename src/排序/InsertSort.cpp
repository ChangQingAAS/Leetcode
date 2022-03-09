#include <iostream>
#include <vector>
using namespace std;

void insert_sort(vector<int> &nums, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j > 0; j--)
        {
            if (nums[j] < nums[j - 1])
                swap(nums[j], nums[j - 1]);
            else
                break;
        }
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
    int n = nums.size();
    insert_sort(nums, n);
    print_array(nums);
}