class NumArray
{
public:
    vector<int> psum;
    NumArray(vector<int> &nums)
    {
        psum.assign(nums.size() + 1, 0);
        for (int i = 1; i <= nums.size(); i++)
        {
            psum[i] = psum[i - 1] + nums[i - 1];
        }
    }

    int sumRange(int left, int right)
    {
        return psum[right + 1] - psum[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */