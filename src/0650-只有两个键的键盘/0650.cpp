class Solution {
public:
    int minSteps(int n) {
      int * dp = (int *)calloc(sizeof(int), n+1);
      for (int i = 2; i<= n;i++){
        dp[i] = i;
        for (int j = 2; j<= sqrt(i); j++){
          if(i % j == 0){
            dp[i] = dp[j] + dp[i/j];
            break;
          }
        }
      }
      return dp[n];
    }
};
