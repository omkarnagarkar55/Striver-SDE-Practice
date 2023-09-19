class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        m = {}
        for i in range(0,len(nums)):
            val = target - nums[i]
            if val in m.keys():
                ans.append(i)
                ans.append(m[val])
            else:
                m[nums[i]] = i

        return ans
