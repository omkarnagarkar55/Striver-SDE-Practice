class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(1, len(height)-1):
            leftMax = max(height[0:i])
            rightMax = max(height[i+1:])
            if leftMax > height[i] and rightMax > height[i]:
                ans += min(leftMax , rightMax) - height[i]
        return ans