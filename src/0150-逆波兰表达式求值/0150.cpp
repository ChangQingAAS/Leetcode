class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> stack;
        int res;
        for (int i = 0; i < tokens.size(); i++)
        {
            if (tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/")
            {
                int num1 = stack.top();
                stack.pop();
                int num2 = stack.top();
                stack.pop();

                if (tokens[i].compare("+") == 0)
                {
                    res = num2 + num1;
                }
                else if (tokens[i].compare("-") == 0)
                {
                    res = num2 - num1;
                }
                else if (tokens[i].compare("*") == 0)
                {
                    res = num2 * num1;
                }
                else if (tokens[i].compare("/") == 0)
                {
                    res = num2 / num1;
                }

                stack.push(res);
            }
            else
            {
                // 字符转数字
                stack.push(stoi(tokens[i]));
            }
        }

        // 防备只有一个数字的情况
        res = stack.top();
        return res;
    }
};