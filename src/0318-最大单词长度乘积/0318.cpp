class Solution {
public:
    int maxProduct(vector<string>& words) {
      int n = words.size();
      vector<int> hash(n,0);
      int ans = 0;
      for (int i = 0; i< n; i++){
        for(const char & c : words[i]){
          hash[i] |= 1 << (c - 'a');
        }
      }
      
      for (int i = 0; i < n-1; i++){
        for(int j = i+1; j < n; j++){
          if( !(hash[i] & hash[j]) ){
            ans = max(ans, int(words[i].length() * words[j].length()));
          }
        }
      }
    return ans;
    }
};
