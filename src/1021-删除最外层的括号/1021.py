class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = ''
        # 遍历字符串

# 左括号入栈：若入栈后栈的长度大于1，即该左括号不是原语首个左括号，结果加入'('
# 右括号出栈：若出栈后栈的长度大于0，即该右括号不是原语末个右括号，结果加入')'
        for i in s:
            if i == '(':
                stack.append(i)
                if len(stack) > 1:
                    result += '('
            else:
                stack.pop()
                if len(stack) != 0:
                    result += ')'

        return result