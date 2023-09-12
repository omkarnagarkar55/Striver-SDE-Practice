
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        limit = len(nums)//3
        ans = []
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] = counter[i] + 1
            if counter[i] > limit:
                if i not in ans:
                    ans.append(i)
        return ans