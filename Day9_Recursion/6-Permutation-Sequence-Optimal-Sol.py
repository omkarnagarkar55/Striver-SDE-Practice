class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ''
        fact = 1
        nums = []
        # Calculating factorial (n-1)! and storing nums in list
        for i in range(1,n):
            fact*=i
            nums.append(i)

        nums.append(n)
        # Start index of our array is 0
        k = k-1
        while True:
            ans+=str(nums[int(k/fact)])
            nums.remove(nums[int(k/fact)])
            if len(nums) == 0:
                break
            k = k % fact
            fact = fact/len(nums)
        
        return ans