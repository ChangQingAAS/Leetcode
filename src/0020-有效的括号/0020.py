class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char not in ['(','{','[']:
                if not stack:
                    return False

                elif (stack[-1] + char) not in ('()','{}','[]'):
                    return False
                
                stack.pop()
            else:
                stack.append(char)
        return not stack