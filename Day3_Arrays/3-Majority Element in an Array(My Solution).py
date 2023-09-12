import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        ans = None
        limit = math.floor(len(nums)/2)
        for i in nums:
            if i in count:
                count[i]=count[i]+1
            else:
                count[i]= 1
            if count[i] > limit:
                ans = i
                break
        return ans