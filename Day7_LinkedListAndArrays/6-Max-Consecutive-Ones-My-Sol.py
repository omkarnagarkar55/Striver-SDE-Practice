class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max= -1
        c = 0
        for i in nums:
            if i == 1:
                c+=1
            else:
                if max < c:
                    max = c
                c=0
        if max< c:
            max = c
        return max