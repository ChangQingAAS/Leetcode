class Solution {
public:
    bool isPowerOfThree(int n) {
    // log(3)(n) = m为整数
      return fmod(log10(n) / log10(3), 1) == 0;

    }
};
