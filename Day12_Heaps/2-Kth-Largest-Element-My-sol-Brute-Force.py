class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range((n-1)//2,-1,-1):
            self.heapify(nums,i,n)

        for i in range(n-1,-1,-1):
            nums[0],nums[i] = nums[i],nums[0]
            if i == n - k :
                return nums[i]
            self.heapify(nums,0,i)

    def heapify(self,nums,i,n):
        left = 2 * i + 1
        right = 2 * i + 2

        mid = i

        if left < n and nums[i] < nums[left]:
            mid = left
        
        if right < n and nums[right] > nums[mid]:
            mid = right
        
        if mid != i:
            nums[i], nums[mid] = nums[mid], nums[i]
            self.heapify(nums, mid,n)