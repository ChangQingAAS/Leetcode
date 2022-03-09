#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

bool canPartition(vector<int> &nums)
{
    int n = nums.size();
    if (n < 2)
        return false;
    int sum = accumulate(nums.begin(), nums.end(), 0);
    if (sum % 2)
        return false;
    int target = sum / 2;
    vector<vector<bool>> dp(n + 1, vector<bool>(target + 1, false));
    for (int i = 0; i <= n; i++)
    {
        dp[i][0] = true;
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= target; j++)
        {
            if (j < nums[i - 1])
            {
                dp[i][j] = dp[i - 1][j];
            }
            else
            {
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
            }
        }
    }

    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= target; j++)
        {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }

    return dp[n][target];
}

int main()
{
    vector<int> nums = {1, 5, 10, 6};
    canPartition(nums);
}