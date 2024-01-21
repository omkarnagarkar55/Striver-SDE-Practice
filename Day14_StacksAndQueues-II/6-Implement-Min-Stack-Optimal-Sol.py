class MinStack:
    # TC -O(1) for all function call and SC - O(n)
    def __init__(self):
        self.stack  = []
        self.m = float('inf')        

    def push(self, val: int) -> None:
        if self.stack:
            # If val to be pushed is smaller than the min then modify it using formula and push on to the stack or else just push the element.
            if self.m > val:
                minval = 2 * val - self.m
                self.stack.append(minval)
                self.m = val
            else:
                self.stack.append(val)
        else:
            self.stack.append(val)
            self.m = val

    def pop(self) -> None:

        if self.stack[-1] < self.m:
            # Removing the modified element and updating the min
            self.m = 2 * self.m - self.stack[-1]
        self.stack.pop()
            
    def top(self) -> int:
        if self.stack[-1] < self.m:
            return self.m
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()