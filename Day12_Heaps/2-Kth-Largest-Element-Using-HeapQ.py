import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = []
        for i in range(n):
            heapq.heappush(ans, -nums[i])
        
        a = k - 1
        while(a > 0):
            heapq.heappop(ans)
            a-=1
        return -ans[0]