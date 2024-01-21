class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if len(self.stack) == 0:
            self.stack.append(price)
            return 1
        c = 1
        s =[]
        while self.stack and self.stack[-1] <= price:
            c+=1
            temp = self.stack.pop()
            s.append(temp)
        
        while s:
            self.stack.append(s.pop())
        self.stack.append(price)    
        return c


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)