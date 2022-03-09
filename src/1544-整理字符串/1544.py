class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for item in s:
            if not stack:
                stack.append(item)
                continue

            while stack:
                ele = stack.pop()
                if ord(ele) - ord(item) == 32 or ord(item) - ord(ele) == 32:
                    break
                else:
                    stack.append(ele)
                    stack.append(item)
                    break

        return ''.join(stack)