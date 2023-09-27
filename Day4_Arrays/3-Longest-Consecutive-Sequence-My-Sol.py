class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        maxi= -1

        if len(nums) != 0:
            count = 1
            for i in range(len(nums)-1):
                if nums[i] + 1 == nums[i+1]:
                    count+=1
                elif nums[i] == nums[i+1]:
                    continue
                else:
                    if maxi < count:
                        maxi= count
                    count = 1

        if maxi < count:
            maxi= count
        return maxi