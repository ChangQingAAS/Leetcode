class TrieNode
{
public:
    TrieNode *childNode[26];
    bool isVal;
    TrieNode() : isVal(false)
    {
        for (int i = 0; i < 26; i++)
        {
            childNode[i] = nullptr;
        }
    }
};

class Trie
{
    TrieNode *root;

public:
    Trie() : root(new TrieNode())
    {
    }

    void insert(string word)
    {
        TrieNode *temp = root;
        for (int i = 0; i < word.size(); i++)
        {
            if (!temp->childNode[word[i] - 'a'])
            {
                temp->childNode[word[i] - 'a'] = new TrieNode();
            }
            temp = temp->childNode[word[i] - 'a'];
        }
        temp->isVal = true;
    }

    bool search(string word)
    {
        TrieNode *temp = root;
        for (int i = 0; i < word.size(); i++)
        {
            if (!temp)
            {
                break;
            }
            temp = temp->childNode[word[i] - 'a'];
        }
        return temp ? temp->isVal : false;
    }

    bool startsWith(string prefix)
    {
        TrieNode *temp = root;
        for (int i = 0; i < prefix.size(); ++i)
        {
            if (!temp)
            {
                break;
            }
            temp = temp->childNode[prefix[i] - 'a'];
        }
        return temp;
    }
};