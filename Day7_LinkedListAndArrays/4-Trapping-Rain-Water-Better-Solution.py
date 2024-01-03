class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        pre = []
        suf = []
        maxi = -1
        maxi2 = -1
        for i in range(len(height)):
            maxi = max(maxi,height[i])
            pre.append(maxi)

        for i in range(len(height)-1,-1,-1):
            maxi2 = max(maxi2,height[i])
            suf.append(maxi2)    

        for i in range(1, len(height)-1):
            leftMax = pre[i-1]
            rightMax = suf[::-1][i+1]
            if leftMax > height[i] and rightMax > height[i]:
                ans += min(leftMax , rightMax) - height[i]
        return ans