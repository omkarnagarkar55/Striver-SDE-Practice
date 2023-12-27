class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        l = set()
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        ll= [nums[i],nums[j],nums[k]]
                        ll.sort()
                        l.add(tuple(ll))

        return [list(e) for e in l]