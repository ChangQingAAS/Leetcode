class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue
            elif stack[-1] == char:
                stack.pop()
                continue
            stack.append(char)
        return ''.join(stack)