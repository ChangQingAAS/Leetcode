class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for item in logs:
            if item == '../':
                if stack:
                    stack.pop()
            elif item == './':
                pass
            else:
                stack.append(item)
        return len(stack)