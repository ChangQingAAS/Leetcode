/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var canPartition = function(nums) {
    const length = nums.length;
    if(length<2)
        return false;
    let sum = 0;

    let maxNum = 0;
    for(let i=0; i<length; i++){
        sum+=nums[i];
        if(nums[i]>maxNum){
            maxNum = nums[i]
        }
    }

    //
    if(sum & 1)
        return false;

    const target = sum/2;
    if(maxNum>target)
        return false;


    let dp = new Array(length);

    //initial dp array
    for(let i=0;i<length;i++){
        dp[i] = new Array(target+1);
        for(let j=0;j<=target;j++){
            dp[i][j] = false;
        }
    }

    //set dp[i][0] = 1 because no value is selected
    for(let i=0;i<length;i++){
        dp[i][0] = true;
    }

    //initial
    dp[0][nums[0]] = true;

    //dp

    for(let i=1;i<length;i++){
        let num = nums[i];
        for(let j=1;j<=target;j++){
            if(j<num){
                dp[i][j] = dp[i-1][j];
            }else{
                dp[i][j] = dp[i-1][j-num] | dp[i-1][j];
            }
        }
    }

    return dp[length-1][target];
}; 