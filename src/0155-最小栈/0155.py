class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = None
    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        else:
            self.min = min(self.min,val)
        self.stack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min = min(self.stack)
        else:
            self.min = None
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min
 