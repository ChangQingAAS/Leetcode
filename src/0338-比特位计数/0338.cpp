class Solution {
public:
    vector<int> countBits(int n) {
      vector<int> dp(n + 1, 0);
      for(int i = 1; i<=n;i++){
        dp[i] = i & 1 ?  dp[i-1] + 1 : dp[i>>1];
      }
      return dp;
    }
};

// 其中 dp[i] 表示数字 i的二进制含有 1 的个数。对于第 i 个数字，如果它二进制的最后一位为 1，那么它含有 1 的个数则为 dp[i-1] + 1；如果它二进制的最后一位为 0，那么它含有 1 的个数和其算术右移结果相同，即dp[i>>1]
