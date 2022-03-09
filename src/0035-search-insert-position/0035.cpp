class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

        /* 1.目标值在数组所有元素之前
        # 2.目标值等于数组中元素
        # 3.目标值介于数组元素之间
        # 4.目标值在数组所有元素之后*/
        int length =  nums.size() ;
        for(int i = 0; i < length; i++)
        {
            if(nums[i] >= target)
            {
                return i;
            }
        } 
        return length;

    }
};