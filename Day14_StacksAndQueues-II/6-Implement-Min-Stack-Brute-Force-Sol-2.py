class MinStack:
    # TC -O(1) for all function call and SC - O(2n)
    def __init__(self):
        self.stac  = []
        self.t = -1        

    def push(self, val: int) -> None:
        if self.t != -1:
            minval = min(self.stac[self.t][1],val)
            self.stac.append([val,minval])
        else:
            self.stac.append([val,val])
        self.t += 1

    def pop(self) -> None:
        self.stac.pop()
        self.t -= 1
            
    def top(self) -> int:
        return self.stac[self.t][0]

    def getMin(self) -> int:
        return self.stac[self.t][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()