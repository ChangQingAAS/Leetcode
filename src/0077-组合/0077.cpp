class Solution
{
public:
    vector<vector<int>> combine(int n, int k)
    {
        vector<vector<int>> ans;
        vector<int> comb(k, 0);
        int count = 0;
        backtracking(ans, comb, count, 1, n, k);
        return ans;
    }

    void backtracking(vector<vector<int>> &ans, vector<int> &comb, int &count, int pos, int n, int k)
    {

        if (count == k)
        {
            ans.push_back(comb);
            return;
        }
        for (int i = pos; i <= n; ++i)
        {
            comb[count++] = i; //修改当前节点状态
            backtracking(ans, comb, count, i + 1, n, k);
            --count;
        }
    }
};