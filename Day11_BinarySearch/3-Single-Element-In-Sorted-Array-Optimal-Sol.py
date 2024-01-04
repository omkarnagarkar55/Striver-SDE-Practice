class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        
        # If length of list 1 then simply return the element 
        if n == 1:
            return nums[0]
        
        # Binary search
        while(low <= high):
            mid = (low + high) >> 1

            # If mid is the first index
            if mid == 0 and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
            # If mid is the last index
            elif mid == n - 1 and nums[mid]!=nums[mid-1]:
                return nums[mid]
            
            # Condition for middle element
            if nums[mid]!=nums[mid - 1] and nums[mid]!=nums[mid + 1]:
                return nums[mid]
            
            # Even Odd Index check 
            if (mid - 1) % 2 == 0 and nums[mid] == nums[mid - 1] or mid % 2 == 0 and nums[mid] == nums[mid + 1]:

                low = mid + 1
            else:
                high = mid - 1

        return -1