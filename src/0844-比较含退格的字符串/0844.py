class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        for item in s:
            if item == '#' and s_stack:
                s_stack.pop()
            if item != '#':
                s_stack.append(item)

        t_stack = []
        for item in t:
            if item == '#' and t_stack:
                t_stack.pop()
            if item != '#':
                t_stack.append(item)
        
        return s_stack == t_stack