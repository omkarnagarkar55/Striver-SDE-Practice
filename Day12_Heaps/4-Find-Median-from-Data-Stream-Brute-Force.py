import heapq
class MedianFinder:

    def __init__(self):
        self.ans = []
        heapq.heapify(self.ans)

    def addNum(self, num: int) -> None:
        self.ans.append(num)
        print(num)

    def findMedian(self) -> float:
        n = len(self.ans)
        self.ans.sort()
        if n % 2 == 1:
            return self.ans[(n - 1)//2]
        else:
            return (self.ans[(n - 1)//2] + self.ans[n//2])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()