import heapq
class MedianFinder:

    def __init__(self):
        self.num1 = []
        self.num2 = []

    def addNum(self, num: int) -> None:
        # If length of num1 and num2 is 0. Then add the element in num1.
        if len(self.num1) == 0 and len(self.num2) == 0 :
            heapq.heappush(self.num1, -num)
        else:
            if -self.num1[0] >= num:
                heapq.heappush(self.num1, -num)
            else:
                heapq.heappush(self.num2, num)
                
            # Reshuffle if length of num1 becomes greater than len(num2) + 1
            if len(self.num1) == len(self.num2) + 2:
                temp = -heapq.heappop(self.num1)
                heapq.heappush(self.num2,temp)

            elif len(self.num1) < len(self.num2):
                temp = heapq.heappop(self.num2)
                heapq.heappush(self.num1,-temp)

    def findMedian(self) -> float:
        n = len(self.num1) + len(self.num2)
        if n % 2 == 1:
            return -self.num1[0]
        else:
            return (-self.num1[0] + self.num2[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()