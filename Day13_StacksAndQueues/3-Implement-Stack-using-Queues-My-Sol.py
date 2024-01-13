class MyStack:

    def __init__(self):
        self.arr = []
        self.i = -1

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.i += 1

    def pop(self) -> int:
        item = self.arr.pop()
        self.i -= 1
        return item

    def top(self) -> int:
        return self.arr[self.i]

    def empty(self) -> bool:
        if self.i == -1:
            return True
        else:
            return False
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()