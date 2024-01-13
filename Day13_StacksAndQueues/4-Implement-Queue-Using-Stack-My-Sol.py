class MyQueue:

    def __init__(self):
        self.arr = []
        self.i = -1

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.i += 1

    def pop(self) -> int:
        i = self.i
        arr1 = []
        while i>0:
            arr1.append(self.arr.pop())
            i -= 1
        item = self.arr.pop()
        self.i -= 1

        j = self.i
        
        while j>=0:
            self.arr.append(arr1.pop())
            j -= 1
        return item
        
    def peek(self) -> int:
        i = self.i
        arr1 = []
        while i>=0:
            arr1.append(self.arr[i])
            i-=1
        return arr1[self.i]

    def empty(self) -> bool:
        if self.i == -1:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()