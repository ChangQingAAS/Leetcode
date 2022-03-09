class Solution {
    vector<int> origin;
public:
    Solution(vector<int>& nums):origin(std::move(nums)){
    
    }
    
    vector<int> reset() {
      return origin;
    }
    
    vector<int> shuffle() {
      if(origin.empty()) return {};
      vector<int> shuffled(origin);
      int n = origin.size();
      for (int i = n - 1; i>=0; i--){
        swap(shuffled[i], shuffled[rand() %(i + 1)]);
      }
      return shuffled;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
