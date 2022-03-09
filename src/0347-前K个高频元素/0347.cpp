class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        // 找最大count
        unordered_map<int, int> counts;
        int max_count = 0;
        for (const int &num : nums)
        {
            max_count = max(max_count, ++counts[num]);
        }

        // 把每个数组元素的数量放入buckets
        vector<vector<int>> buckets(max_count + 1);
        for (const auto &p : counts)
        {
            buckets[p.second].push_back(p.first);
        }

        vector<int> ans;
        for (int i = max_count; i >= 0 && ans.size() < k; i--)
        {
            for (const int &num : buckets[i])
            {
                ans.push_back(num);
                if (ans.size() == k)
                {
                    break;
                }
            }
        }

        return ans;
    }
};

//与其说是桶排序，不如说是反向索引