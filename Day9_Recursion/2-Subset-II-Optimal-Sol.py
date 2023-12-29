class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        n =len(nums)
        nums.sort()
        def subSet(ind):
            ans.append(ds[:])
            for i in range(ind,n):
                if i!=ind and nums[i-1] == nums[i]:
                    continue
                ds.append(nums[i])
                subSet(i + 1)
                ds.pop()

        subSet(0)

        return ans