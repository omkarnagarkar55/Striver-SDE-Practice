class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        n = len(nums)

        def genPermu(nums):

            if len(nums) == 2:
                ans.append(ds[:] + [nums[0],nums[1]])
                ans.append(ds[:] + [nums[1],nums[0]])
                return

            if len(nums) == 0:
                ans.append(ds[:])
                return

            for i in range(len(nums)):
                ds.append(nums[i])
                genPermu(nums[0:i]+nums[i+1:])
                ds.pop()
        
        genPermu(nums)
        return ans