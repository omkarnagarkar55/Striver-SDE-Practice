class MinStack:

    def __init__(self):
        self.stac  = []
        self.t = -1        

    def push(self, val: int) -> None:
        self.stac.append(val)
        self.t += 1

    def pop(self) -> None:
        self.stac.pop()
        self.t -= 1
            
    def top(self) -> int:
        return self.stac[self.t]

    def getMin(self) -> int:
        return min(self.stac)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()