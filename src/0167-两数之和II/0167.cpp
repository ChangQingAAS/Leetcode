// 双指针法
class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int left = 0, right = numbers.size() - 1;
        int sum;
        while (left < right)
        {
            sum = numbers[left] + numbers[right];
            if (sum == target)
                break;
            else if (sum < target)
                left++;
            else
                right--;
        }
        return vector<int>{left + 1, right + 1};
    }
};