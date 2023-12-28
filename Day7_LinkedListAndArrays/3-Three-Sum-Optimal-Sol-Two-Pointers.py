class Solution:
    # Approach:- Using Two Pointers
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # Using set to store unique elements
        l = set()
        nums.sort()

        for i in range(n):
            left = i + 1
            right = n - 1
            while(left < right):
                val = nums[i] + nums[left] + nums[right]
                if val > 0:
                    right-=1
                elif val < 0:
                    left+=1
                else:
                    ll= [nums[i] ,nums[left] ,nums[right]]
                    l.add(tuple(ll))
                    left+=1
                    right-=1

        return [list(e) for e in l]