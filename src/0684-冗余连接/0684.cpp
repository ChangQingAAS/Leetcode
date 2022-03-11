class UF
{
    vector<int> id;

public:
    UF(int n) : id(n)
    {
        iota(id.begin(), id.end(), 0); // iota可以把数组初始化为0~n-1
    }
    int find(int p)
    {
        while (p != id[p])
        {
            p = id[p];
        }
        return p;
    }
    void connect(int p, int q)
    {
        id[find(p)] = find(q);
    }
    bool isConnected(int p, int q)
    {
        return find(p) == find(q);
    }
};

class Solution
{
public:
    vector<int> findRedundantConnection(vector<vector<int>> &edges)
    {
        int n = edges.size();
        UF uf(n + 1);
        for (auto e : edges)
        {
            int u = e[0], v = e[1];
            if (uf.isConnected(u, v))
            {
                return e; //说明此时有环
            }
            uf.connect(u, v);
        }
        return vector<int>{-1, -1};
    }
};