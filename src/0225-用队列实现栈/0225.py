from queue import Queue

class MyStack:

    def __init__(self):
        self.stack = Queue()
        self.top_elem = None

    def push(self, x: int) -> None:
        self.stack.put(x)
        self.top_elem = x

    def pop(self) -> int:
        size = self.stack.qsize()
        while size > 1:
            elem = self.stack.get()
            self.stack.put(elem)
            self.top_elem = elem
            size -= 1
        return self.stack.get()

    def top(self) -> int:
        return self.top_elem

    def empty(self) -> bool:
        if self.stack.qsize():
            return False
        return True

# * 队列先进先出
# * 栈后进先出
# * 一个队列在模拟栈弹出元素的时候只要将队列头部的元素（除了最后一个元素外） 重新添加到队列尾部，此时在去弹出元素就是栈的顺序了

# ![](https://cdn.jsdelivr.net/gh/ChangQingAAS/for_picgo/img/20211005170800.gif)

