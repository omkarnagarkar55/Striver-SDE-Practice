import heapq
class Solution:
    #TC - O(n+nlogn+klogn) and SC - O(n + k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        ans = []
        pq = []

        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        
        for i in h:
            heapq.heappush(pq,[-h[i],i])

        for i in range(k):
            temp = heapq.heappop(pq)
            ans.append(temp[1])
        return ans