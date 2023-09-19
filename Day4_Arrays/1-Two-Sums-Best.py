class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        left = 0
        right = len(nums) - 1

        while(left < right):
            add = nums[left] + nums[right]
            if add == target:
                ans.append(left)
                ans.append(right)
            else:
                if add < target:
                    left=left + 1
                else:
                    right=right - 1

        return ans



