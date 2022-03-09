class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
      // dp[i][j] 表示到第一个字符串位置 i 为止、到第二个字符串位置 j 为止、最长的公共子序列长度
      int m = text1.length(), n = text2.length();
      vector<vector<int>> dp(m+1, vector<int>(n + 1, 0));
      for (int i = 1; i<=m; i++){
        for(int j = 1; j <= n; j++){
          if (text1[i-1] == text2[j-1]){
            dp[i][j] = dp[i-1][j-1] + 1;
          }else{
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]);
          }
        }
      }
      return dp[m][n];
    }
};
