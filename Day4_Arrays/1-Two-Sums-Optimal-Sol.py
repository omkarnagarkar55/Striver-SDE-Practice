class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0,len(nums)):
            val= target - nums[i]
            if val in nums and nums.index(val)!=i:
                ans.append(i)
                ans.append(int(nums.index(val)))
                break
        return ans
