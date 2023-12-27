class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        b = 1
        count = 0
        # Replacing Duplicates with _
        while(b<n):
            if nums[a] == nums[b]:
                nums[b] = "_"
                b+=1
                count+=1
            else:
                a = b
                b += 1

        # Moving all the Integers to the left side
        k = n-count
        a = b = 0
        while(a<k and b < n):
            if nums[b]=='_':
                b+=1
            else:
                nums[a] = nums[b]
                a+=1
                b+=1
        return k