class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        b = 1
        count = 0
        while(b<n):
            if nums[a] == nums[b]:
                nums[b] = "_"
                b+=1
                count+=1
            else:
                a = b
                b += 1
    
        print(nums)
        print(n-count)
        for i in range(count):
            nums.remove('_')
        return n-count