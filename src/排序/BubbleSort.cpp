#include <iostream>
#include <vector>
using namespace std;

void bubble_sort(vector<int> &nums, int n)
{
    bool swapped;
    for (int i = 0; i < n - 1; i++)
    {
        swapped = false;
        for (int j = 0; j < n - 1 - i; j++)
        {
            if (nums[j + 1] < nums[j])
            {
                swap(nums[j], nums[j + 1]);
                swapped = true;
            }
        }
        if (!swapped)
        {
            break;
        }
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
    int n = nums.size();
    bubble_sort(nums, n);
    print_array(nums);
}