class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n =len(nums)
        nums.sort()
        def subSet(ind , subarray):
            if ind == n:
                ans.add(tuple(subarray))
                return
            
            else:
                subSet(ind + 1 , subarray + [nums[ind]])

                subSet(ind + 1 , subarray)
        
            return
        
        subSet(0,[])

        return [list(item) for item in ans]