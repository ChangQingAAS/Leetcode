class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size(); //原二维数组的长
        int n = mat[0].size(); //原二维数组的宽
        if (m * n != r * c) //对比两个二维数组的总数多少，如果不一样直接返回原来的。
        {
            return mat;
        }
        vector<vector<int>> ans (r,vector<int>(c));
        for(int i = 0; i < m * n; i++)
        {
            ans[i / c][i % c] = mat[i / n][i % n];
        }
        return ans;
    }
};