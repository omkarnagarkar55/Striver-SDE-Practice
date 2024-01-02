class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        ds = []
        nums = [i for i in range(1,n+1)]

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
        an= ''
        for i in ans[k-1]:
            an +=str(i)
        return an