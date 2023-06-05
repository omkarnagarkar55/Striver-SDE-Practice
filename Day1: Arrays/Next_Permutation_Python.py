class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l =len(nums)
        if l == 2:
            if nums[1] > nums[0]:
                temp = nums[1]
                nums[1] = nums[0]
                nums[0] = temp
        elif l>2:
            i = l -2
            while(i>=0):
                if nums[i] >= nums[i+1]:
                    i-=1
                else:
                    break
            if i >=0:
                j= i+1
                close =0
                while(j<l):
                    diff = 9999
                    if nums[i]<nums[j] and nums[j]-nums[i] <diff:
                        diff = nums[j]-nums[i]
                        close = j
                    j+=1
                    
                temp = nums[close]
                nums[close] =nums[i]
                nums[i] = temp
                nums[i+1:l] = nums[i+1:l][::-1]
                
            else:
                nums.sort()
                
                    
            
        
