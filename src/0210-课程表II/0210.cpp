class Solution
{
public:
    vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites)
    {
        vector<vector<int>> graph(numCourses, vector<int>());
        vector<int> indegree(numCourses, 0), res;
        for (const auto &prerequisite : prerequisites)
        {
            graph[prerequisite[1]].push_back(prerequisite[0]);
            indegree[prerequisite[0]]++;
        }
        queue<int> q;
        for (int i = 0; i < indegree.size(); i++)
        {
            if (!indegree[i])
            {
                q.push(i);
            }
        }
        while (!q.empty())
        {
            int u = q.front();
            res.push_back(u);
            q.pop();
            for (auto v : graph[u])
            {
                indegree[v]--;
                if (!indegree[v])
                {
                    q.push(v);
                }
            }
        }
        // 对于存在环的情况
        for (int i = 0; i < indegree.size(); i++)
        {
            if (indegree[i])
            {
                return vector<int>();
            }
        }
        return res;
    }
};