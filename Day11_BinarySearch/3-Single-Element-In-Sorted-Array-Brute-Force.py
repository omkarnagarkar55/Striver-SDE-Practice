class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)  # Size of the array
        if n == 1:
            return nums[0]

        for i in range(n):
            # Check for first index
            if i == 0:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            # Check for last index
            elif i == n - 1:
                if nums[i] != nums[i - 1]:
                    return nums[i]
            else:
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    return nums[i]
        