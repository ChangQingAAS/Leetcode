class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # 往队列中添加元素
        self.stack_in.append(x)

    def pop(self) -> int:
        # 从队列中取出一个元素
        if not self.stack_out:
            self.stack_out = self.stack_in[:: -1]
            self.stack_in = []
        return self.stack_out.pop()

    def peek(self) -> int:
        # 获取队列的头部
        if not self.stack_out:
            self.stack_out = self.stack_in[::-1]
            self.stack_in = []
        return self.stack_out[-1]

    def empty(self) -> bool:
        # 判断队列是否为空
        if self.stack_out or self.stack_in:
            return False
        return True 